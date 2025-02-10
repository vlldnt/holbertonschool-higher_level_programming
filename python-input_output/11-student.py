#!/usr/bin/python3
'''Class Students creation'''


class Student:
    '''Student class'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            if all(isinstance(obj, str) for obj in attrs):
                return {key: value for key, value in
                        self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for keys, values in json.items():
            setattr(self, keys, values)
