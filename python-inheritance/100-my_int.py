#!/usr/bin/python3
'''MyInt is rebel'''

class MyInt(int):
    '''rebel int'''

    def equal(self, value):
        if self == value:
            return False
        return True
