#!/usr/bin/python3
"""post request module"""
import requests
from sys import argv


if __name__ == "__main__":
    # hdrsi = {'Authorization': "Bearer {}".format(argv[2])}
    req = requests.get("https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2]))
    try:
        for dct in req.json():
            print(dct['sha'], dct['name'])
    except Exception:
        print(None)
