#!/usr/bin/python3
"""response header module"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    try:
        print(req.headers['X-Request-Id'])
    except KeyError:
        pass
