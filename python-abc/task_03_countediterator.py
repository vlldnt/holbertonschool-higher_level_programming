#!/usr/bin/python3
''' Keep track of iteration'''


class CountedIterator:
    '''Extends the built in iterator from iter'''

    def __init__(self, data):
        self.i = 0
        self.iterator = iter(data)

    def get_count(self):
        return self.i

    def __next__(self):
        self.i += 1
        return next(self.iterator)
