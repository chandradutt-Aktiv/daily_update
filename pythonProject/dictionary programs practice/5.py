"""
Write a Python program to iterate over
dictionaries using for loops.
"""
import types
import datetime

print(types)

print(datetime)

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print(type(d.keys()))

print(type(d.values()))

for i, j in d.items():

    print(i, j)
