from pathlib import Path
import mkdocs_gen_files

src = Path("api/src")

for path in sorted(src.rglob("*.py")):
    doc_path = Path(str(path.relative_to(src).with_suffix(".md")).replace("__", ""))
    parts = list(Path(path.relative_to(src).with_suffix("")).parts)

    print(parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]

    with mkdocs_gen_files.open(doc_path, "w") as f:
        identifier = ".".join(parts)
        print(f"::: {identifier}", file=f)
    
