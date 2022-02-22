"""By using list comprehension, please write a program to print the list after
 removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]."""

l=[12,24,35,70,88,120,155]
p=[0,2,4,6]

l1=[l[i] for i in range(len(l)) if i not in p]
print(l1)