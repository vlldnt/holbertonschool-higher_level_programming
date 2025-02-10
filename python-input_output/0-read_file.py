#!/usr/bin/python3
'''Read file and print'''


def read_file(filename=""):
    with open(filename) as file:
        for words in file:
            print("{}".format(words), end="")
