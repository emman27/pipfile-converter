# Pipfile Converter
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Femman27%2Fpipfile-converter.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Femman27%2Fpipfile-converter?ref=badge_shield)


Converts your `Pipfile` into a regular `requirements.txt` for usage in `pip install`

At the moment, uses Pipfile.lock instead of Pipfile. This ensures you always get back the same version as the original

### Usage
```
pip install $(python parser.py --file ~/<path>/Pipfile.lock)
```
Default path if not specified is Pipfile.lock in your current directory


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Femman27%2Fpipfile-converter.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Femman27%2Fpipfile-converter?ref=badge_large)