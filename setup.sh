python3 setup.py sdist bdist_wheel
python3 -m pip install -U twine
python3 -m twine upload dist/*