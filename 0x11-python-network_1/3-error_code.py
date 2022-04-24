#!/usr/bin/python3
"""get header module"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            page = response.read()
    except error.HTTPError as e:
        print("Error code: " + str(e.code))
    else:
        print(page.decode("utf-8"))
