#!/usr/bin/python3
"""get header module"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({'email': argv[2]}).encode()
    req = request.Request(argv[1], data=data)
    with request.urlopen(req) as response:
        page = response.read()
    print(page.decode("utf-8"))
