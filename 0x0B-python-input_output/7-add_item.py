#!/usr/bin/python3
""" Add args to JSON file Module """
from os.path import exists
from os import stat
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


lst = []
if exists("add_item.json") and stat("add_item.json").st_size != 0:
    lst = load_from_json_file("add_item.json")
for arg in sys.argv[1:]:
    lst.append(arg)
save_to_json_file(lst, "add_item.json")
