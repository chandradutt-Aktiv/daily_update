""" Write a Python program to find the highest 3 values of corresponding
keys in a dictionary."""

d={"A":3,"Z":5,"B":4,"H":1,"K":8,"T":0}

s=""

#d = sorted(d.keys(),reverse=True)[:4]
for i in sorted(d,reverse=True)[3]:
    s+=i

print(s)
# for i in range(0,3):
#     print(d[i])
print(d)