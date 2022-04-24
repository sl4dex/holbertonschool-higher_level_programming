#!/usr/bin/python3
"""post request module"""
import requests
from sys import argv


if __name__ == "__main__":
    hdrs = {'Authorization': "Bearer {}".format(argv[2])}
    req = requests.get("https://api.github.com/users/{}".format(argv[1]),
                       headers=hdrs)
    try:
        print(req.json()['id'])
    except Exception:
        print(None)
