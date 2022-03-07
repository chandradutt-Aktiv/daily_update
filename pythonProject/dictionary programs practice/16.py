"""
Write a Python program to get a dictionary from an object's fields.
"""


class od:
    def __init__(self):
        self.name = 'chandradutt'
        self.age = '22'
        self.city = 'ahmedabad'

    def p(self):
        pass


obj = od()

print(obj.__dict__)
