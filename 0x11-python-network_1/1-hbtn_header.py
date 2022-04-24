#!/usr/bin/python3
"""get header module"""
import urllib.request
import sys


req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    page = response.getheader("X-Request-Id")
print(page)
