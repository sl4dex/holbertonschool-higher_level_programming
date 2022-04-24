#!/usr/bin/python3
"""get status module"""
import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    page = response.read()
t = type(page)
utf = page.decode("utf-8")
print("Body response:\n\
\t- type: {}\n\
\t- content: {}\n\
\t- utf8 content: {}".format(t, page, utf))
