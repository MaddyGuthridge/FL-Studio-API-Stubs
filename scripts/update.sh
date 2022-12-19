# Push an update to Pypi

rm -rf ./dist

python -m build

python -m twine upload dist/*
