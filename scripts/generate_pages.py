import os
from pathlib import Path
from shutil import copytree, rmtree


def generate():
    # Remove the old docs_build directory
    docs_build_dir = Path("docs_build")
    docs_dir = Path("docs")
    rmtree(docs_build_dir, ignore_errors=True)
    docs_build_dir.mkdir()

    # We need to import this here, otherwise it kinda dies a little
    import mkdocs_gen_files  # noqa: E402 type: ignore

    src = Path("src")
    modules = []

    # Get all modules in the src directory
    for path in src.rglob("*.py"):
        # Get the parent directory of the Python files, which returns the module itself rather than specific files
        module = Path(path.relative_to(src)).parent
        # Make sure no duplicate modules are added
        if module not in modules:
            modules.append(module)

    for module in modules:
        # If there are any modules with submodules, make sure we generate an index page for that module instead of a separate page, then append the markdown file extension
        module_path = (Path(module, "index")
                       if any(m.parent == module for m in modules)
                       else module
                       ).with_suffix(".md")
        with mkdocs_gen_files.open(module_path, "w") as f:
            # Change module path to a dot-separated identifier for mkdocs-gen-files and generate that page
            identifier = ".".join(module.parts)
            print(f"::: {identifier}", file=f)

    def find_duplicates(src: Path, dest: Path) -> list[Path]:
        """
        Returns a list of files that would be overwritten when merging files
        """
        duplicates = []
        for root, dirs, files in os.walk(src):
            for dir in dirs:
                dir_path_src = src.joinpath(dir)
                dir_path_dest = dest.joinpath(dir)
                if dir_path_dest.exists():
                    duplicates.extend(find_duplicates(dir_path_src, dir_path_dest))
            for file in files:
                file_path = dest.joinpath(file)
                if file_path.exists():
                    duplicates.append(file_path)

        return duplicates

    duplicates = find_duplicates(docs_dir, docs_build_dir)
    if len(duplicates):
        print("Unable to generate docs, files would be overwritten")
        for dup in duplicates:
            print(f"- {dup}")
        exit(1)

    # Now go and merge in the docs directory
    copytree(Path("docs"), Path("docs_build"), dirs_exist_ok=True)


if __name__ == "__main__":
    generate()
