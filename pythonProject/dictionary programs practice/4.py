"""
Write a Python script to check whether a given key
already exists in a dictionary.
"""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

k = int(input('enter key value to check it is exist or not: '))

if(k in d.keys()):

    print('exist in dictionary')

else:

    print('not exist ')
