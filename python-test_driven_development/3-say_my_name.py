#!/usr/bin/python3
'''
Print a string with first name with last name
The first name and last name
print the full name
'''


def say_my_name(first_name, last_name=""):
    '''Function that prints name and last name'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
