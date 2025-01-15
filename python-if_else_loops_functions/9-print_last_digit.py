#!/usr/bin/env python3
def print_last_digit(number):
    last = ""
    if number < 0:
        last = number % 10 * -1
    else:
        last = number % 10
    return last
