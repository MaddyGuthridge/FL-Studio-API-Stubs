# Push an update to the script

rm -rf ./dist

python -m build

python -m twine upload dist/*
