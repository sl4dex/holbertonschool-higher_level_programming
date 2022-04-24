#!/usr/bin/python3
"""post request module"""
import requests
from sys import argv


if __name__ == "__main__":
    #q = argv[1] if len(argv) > 1 else ""
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        s = str(req.json())
        d = req.json()
    except JSONDecodeError:
        print("Not a valid JSON")
    else:
        if s == "{}":
            print("No result")
        else:
            print("[{}] {}".format(d['id'], d['name']))
