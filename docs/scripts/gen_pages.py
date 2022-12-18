from pathlib import Path
import mkdocs_gen_files

src = Path("api/src")
modules = []

for path in src.rglob("*.py"):
    module = Path(str(path.relative_to(src)).replace("__", "")).parent
    if module not in modules:
        modules.append(module)

for module in modules:
    print(module)
    with mkdocs_gen_files.open(module.with_suffix(".md"), "w") as f:
        identifier = ".".join(module.parts)
        print(f"::: {identifier}", file=f)
    
