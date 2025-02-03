#!/usr/bin/python3
'''Class MyList that inderits from list'''


class MyList(list):
    '''Return the list created'''
    def print_sorted(self):
        print(sorted(self))
