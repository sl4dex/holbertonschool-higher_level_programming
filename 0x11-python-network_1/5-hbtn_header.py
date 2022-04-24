#!/usr/bin/python3
"""response header module"""
import requests
from sys import argv


req = requests.get(argv[1])
print(req.headers['X-Request-Id'])
