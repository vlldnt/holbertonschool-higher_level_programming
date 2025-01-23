#!/usr/bin/python3
'''
Function that print a square in base size
size is the size of line and row
print it
'''


def print_square(size):
    '''Print the square size #'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
