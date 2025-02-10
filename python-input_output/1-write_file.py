#!/usr/bin/python3
'''Write file in python'''


def write_file(filename="", text=""):
    '''Write a file in python'''
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
    return len(text)
