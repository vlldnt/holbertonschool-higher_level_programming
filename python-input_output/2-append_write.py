#!/usr/bin/python3
'''Append rite a file in python'''


def append_write(filename="", text=""):
    '''Append write a file in python'''
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
    return len(text)
