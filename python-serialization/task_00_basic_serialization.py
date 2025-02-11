#!/usr/bin/python3
'''Serialisze save and deserialize and load filename and data'''


import json


def serialize_and_save_to_file(data, filename):
    '''Serialize and save to file data'''
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    '''Load and deserialize filename'''
    with open(filename, "r") as file:
        return json.load(file)
