from pathlib import Path
import mkdocs_gen_files

src = Path("src")
modules = []

# Get all modules in the src directory
for path in src.rglob("*.py"):
    # Remove '__' from file names to get clean module name for the documentation URLs
    module = Path(str(path.relative_to(src)).replace("__", "")).parent
    # Make sure no duplicate modules are added
    if module not in modules:
        modules.append(module)

for module in modules:
    # If there are any modules with submodules, make sure we generate an index page for that module instead of a separate page, then append the markdown file extension
    module_path = (Path(module, "index") if any(m.parent == module for m in modules) else module).with_suffix(".md")
    with mkdocs_gen_files.open(module_path, "w") as f:
        # Change module path to a dot-separated identifier for mkdocs-gen-files and generate that page
        identifier = ".".join(module.parts)
        print(f"::: {identifier}", file=f)
