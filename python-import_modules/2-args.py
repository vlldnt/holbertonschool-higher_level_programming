#!/usr/bin/python3
from sys import argv
len = len(argv)
if len == 1:
    print("0 arguments.")
elif len == 2:
    print("1 argument:")
else:
    print("{} arguments:".format(len))
for n in range(1, len):
    print("{}: {}".format(n, argv[n]))
