#!/usr/bin/python3
''' Keep track of iteration'''


class CountedIterator:
    '''Extends the built in iterator from iter'''

    def __init__(self, data):
        self.iterator = iter(data)
        self.i = 0

    def get_count(self):
        return self.i

    def __next__(self):
        itered = next(self.iterator)
        self.i += 1
        return itered
