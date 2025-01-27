#!/usr/bin/python3
'''
Creation of an empty class: Square
'''


class Square:
    '''Empty classe named Square'''

    def __init__(self, size=0):
        '''istantiation with size in private'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
