#!/usr/bin/python3
'''Returns an object represented by a JSON string)'''


import json


def from_json_string(my_str):
    '''Workng of JSON string, return'''
    return json.load(my_str)
