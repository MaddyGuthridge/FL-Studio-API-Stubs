from pathlib import Path
import mkdocs_gen_files

src = Path("src")
for path in src.glob("**/*.py"):
    doc_path = Path(str(path.relative_to(src).with_suffix(".md")).replace("__", ""))
    with mkdocs_gen_files.open(doc_path, "w") as f:
        ident = ".".join(path.with_suffix("").parts)
        ident = ident.replace(".__init__", "") if ident.endswith(".__init__") else ident
        print(f"::: {ident}", file=f)