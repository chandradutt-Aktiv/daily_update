"""Please write a program to output a random number, which is divisible
by 5 and 7, between 0 and 10 inclusive using random module and list comprehension."""


import random
for i in range(0,100000):
    print(random.sample([i for i in range(0,1000) if i%5==0 and i%7==0],20))