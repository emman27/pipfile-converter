#!/usr/bin/python
import argparse
import json


def parse(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        d = data['default']
        return ' '.join(['{key}{version}'.format(key=key, version=d[key]['version'])
                         for key in d.keys()])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Converts a Pipfile.lock into a requirements.txt format')
    parser.add_argument('--file', dest='filename', default='./Pipfile.lock', help='filepath')
    args = parser.parse_args()
    print(parse(args.filename))
