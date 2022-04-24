#!/usr/bin/python3
"""get header module"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        page = response.getheader("X-Request-Id")
    print(page)
