#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        print("{:d}".format(my_list[i]), end="\n" if i == x - 1 else "")
        i += 1
    if x > len(my_list):
        return len(my_list)
    return x