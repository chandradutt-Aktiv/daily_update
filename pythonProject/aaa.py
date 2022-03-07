l1 = [1, 2, 3, 10, 12, 14, 16, 20]
l2 = []
for n in l1:
    if n%2 != 0:
        l2.append(n)
        # l1.remove(n)
    else:
        continue
print(l2)
