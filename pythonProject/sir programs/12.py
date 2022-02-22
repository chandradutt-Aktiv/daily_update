"""Please write a program to output a random even number between 0 and 10
inclusive using random module and list comprehension."""

import random

print(random.sample([i for i in range(0,10) if(i%2==0)],5))


"""even = []
l = [even.append(i) for i in range(0,10) if(i%2==0)]

print(even)"""