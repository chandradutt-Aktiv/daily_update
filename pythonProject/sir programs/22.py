"""By using list comprehension, please write a program to print the list after
removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]."""

l,f=[12,24,35,70,88,120,155],[0,4,5]
c = [l[i] for i in range(len(l)) if i not in f]
print(c)