"""By using list comprehension, please write a program generate a 3*5*8
3D array whose each element is 0."""

l=[[['0' for col in range(3)] for col in range(5)] for row in range(8)]
print(l)

