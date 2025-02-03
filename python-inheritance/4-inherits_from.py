#!/usr/bin/python3
''' if object is an instance of
    a class that inherited form a specified class
     but not the class itself'''


def inherits_from(obj, a_class):
    '''Checking function'''
    return isinstance(obj, a_class) and not type(obj) is a_class
