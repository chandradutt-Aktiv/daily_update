from collections import Counter,defaultdict
s='w3resource'
count = defaultdict(int)
for c in s:
    count[c]+=1
print(dict(count))
a ={}
for i in s:
    a[i] =  a.get(i,0)+1
print(a)