"""
Write a Python program to multiply all the items in a dictionary.
"""
d = {1: 1, 2: 4, 3: 9}

mul = 1

for i in d:
    mul = mul * d[i]

print(mul)
