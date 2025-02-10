#!/usr/bin/python3
''' Adds all arguments to a python list and
    save them to a file'''


import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    list = load_from_json_file('add_item.json')
    list.extend(sys.argv[1:])
else:
    list = sys.argv[1:]
save_to_json_file(list, 'add_item.json')
