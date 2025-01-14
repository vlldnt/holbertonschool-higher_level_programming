#!/usr/bin/env python3
def uppercase(str):
    upper = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            upper = upper + chr(ord(c) - 32)
        else:
            upper = upper + c
    print(f"{upper}")
