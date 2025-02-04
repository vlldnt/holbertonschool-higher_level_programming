#!/usr/bin/python3
'''creating a class named BaseGeometry'''


class BaseGeometry:
    '''class BaseGemetry'''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
