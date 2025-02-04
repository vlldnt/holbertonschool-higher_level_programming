#!/usr/bin/python3
'''Abstract class and method'''

from abc import ABC, abstractmethod


class Animal(ABC):
    '''Class animal from ABC'''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''Class Dog from Animal'''
    def sound(self):
        return "Bark"


class Cat(Animal):
    '''Class Cat from Animal'''
    def sound(self):
        return "Meow"
