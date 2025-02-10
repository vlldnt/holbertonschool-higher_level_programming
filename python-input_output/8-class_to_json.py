#!/usr/bin/python3
'''Return vars() or __dict__ of an object'''


def class_to_json(obj):
    return vars(obj)
