#!/usr/bin/python3
'''Class Verbose LIST'''


class VerboseList(list):
    '''VerboseList class from list'''

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] form the list.".format(item))
        super().remove(item)

    def pop(self, item=-1):
        print("Popped [{}] form the list.".format(self[item]))
        return super().pop(item)
