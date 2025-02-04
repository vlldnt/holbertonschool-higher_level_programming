#!/usr/bin/python3
'''creating a class named BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    '''Rectangle class sub from BaseGeometry'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
