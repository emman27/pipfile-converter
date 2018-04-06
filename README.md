# Pipfile Converter

Converts your `Pipfile` into a regular `requirements.txt` for usage in `pip install`

At the moment, uses Pipfile.lock instead of Pipfile. This ensures you always get back the same version as the original

### Usage
```
pip install $(python parser.py --file ~/<path>/Pipfile.lock)
```
Default path if not specified is Pipfile.lock in your current directory
