#!/usr/bin/python3
def add_integer(a, b=98):
    result = 0
    try:
        result = int(a) + int(b)
        raise TypeError("a must be an integer")
    finally:
        return result
