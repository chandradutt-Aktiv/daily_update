"""
Write a Python script to merge two Python dictionaries.
"""

d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

d2 = {12: 144, 13: 169, 14: 196, 15: 225}

d = {}

for i in d1, d2:
    d.update(i)

print(d)
