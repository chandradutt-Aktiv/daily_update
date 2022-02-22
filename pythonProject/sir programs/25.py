"""With a given list [12,24,35,24,88,120,155,88,120,155], write a program to
print this list after removing all duplicate values with original order reserved."""

l=[12,24,35,24,88,120,155,88,120,155]
l1=[]
for i in l:
    if(i not in l1):
        l1.append(i)
print(l1)



t = list(set(l))
print(t)