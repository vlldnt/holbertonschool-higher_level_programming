#!/usr/bin/python3
'''Pickle module for Serialize and deserialize'''


import pickle


class CustomObject:
    '''Pickle module for Serialize and deserialize'''
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''Display dict key value'''
        for key, value in self.__dict__.items():
            print("{}: {}".format(key, value))

    def serialize(self, filename):
        '''Serialize using pickle module to a specified file'''
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''Deserialize filename using pickle module'''
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            return None
