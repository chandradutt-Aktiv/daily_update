"""With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a
program to make a list whose elements are intersection of the above given lists."""

l1=[1,3,6,78,35,55,155]
l2=[12,24,35,24,88,120,155]

t1 = set(l1)
t2 = set(l2)
print(t1)
print(t2)

t = t1.intersection(t2)
print(list(t))