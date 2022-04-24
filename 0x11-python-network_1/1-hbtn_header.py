#!/usr/bin/python3
"""get header module"""
import urllib.request
from sys import argv


req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    page = response.getheader("X-Request-Id")
print(page)
