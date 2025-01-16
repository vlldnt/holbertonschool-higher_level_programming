#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    len = len(argv)
    number = 0
    for i in range(1, len):
        number += int(argv[i])
    print(number)
