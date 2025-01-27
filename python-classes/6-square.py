#!/usr/bin/python3
'''
Creation of an empty class: Square
'''


class Square:
    '''Empty classe named Square'''

    def __init__(self, size=0):
        '''Private istantiation with size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        ''' Calcul of the area of the square
            Public instantiation of area
        '''
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        '''Getter to retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Property setter  to give value to  __size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    def my_print(self):
        '''Print the square based size'''
        if self.__size == 0:
            print()
        else:
            print((("#" * self.__size) + "\n") * self.__size, end="")
