"""Write a Python program to remove a key from a dictionary."""
key = int(input('enter key to remove: '))
d={1: 1, 2: 4, 3: 9}
if(key in d):
    del d[key]
print(d)