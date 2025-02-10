#!/usr/bin/python3
'''Read file and print'''


def read_file(filename=""):
    '''read file and print'''
    with open(filename, "r", encoding="UTF-8") as file:
        for words in file:
            print("{}".format(words), end="")
