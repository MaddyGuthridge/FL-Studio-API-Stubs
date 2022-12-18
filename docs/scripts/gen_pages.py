from pathlib import Path
import mkdocs_gen_files

src = Path("api/src")
modules = []

for path in src.rglob("*.py"):
    module = Path(str(path.relative_to(src)).replace("__", "")).parent
    if module not in modules:
        modules.append(module)

for module in modules:
    module_path = (Path(module, "index") if any(m.parent == module for m in modules) else module).with_suffix(".md")
    print(module_path)
    with mkdocs_gen_files.open(module_path, "w") as f:
        identifier = ".".join(module.parts)
        print(f"::: {identifier}", file=f)
    
