#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    for element in my_list:
        if element not in uniq:
            uniq.append(element)
            sum += element
    return sum
