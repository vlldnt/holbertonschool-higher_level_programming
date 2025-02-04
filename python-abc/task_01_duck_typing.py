#!/usr/bin/python3
'''Duck typing concept'''


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    '''Abstract class ABC'''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''Circle class from shape'''
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return self.radius * 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi


class Rectangle(Shape):
    '''Rectangle class from shape'''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height


def shape_info(shape):
    '''Shape info of shape waribale'''
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
