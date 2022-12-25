from .generate_pages import generate
from mkdocs.commands.build import build as mkdocs_build
from mkdocs.config import load_config


def build():
    generate()
    config = load_config()
    mkdocs_build(config)


if __name__ == "__main__":
    build()
