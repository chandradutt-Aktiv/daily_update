l=[]
n = int(input('how many numbers you have to enter? '))
for i in range(n):
    v = int(input('enter values:- '))
    l.append(v)

print(l)
print(tuple(l))