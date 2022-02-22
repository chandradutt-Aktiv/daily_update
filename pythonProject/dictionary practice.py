#1,2
"""
d = {'z':9, 'x':8,'a':1, 'b':2, 'c':3}
#d1=(sorted(d.values()))
print(d)
d['p']=10
print(d)
"""
#3
"""
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
d4={}
for i in dic1,dic2,dic3:
    d4.update(i)
print(d4)
"""

#4
"""
d = {1:'a',2:'b',3:'c',4:'d',3:'f'}
x=9
if(x in d.keys()):
    print('alreday exist')
else:
    print('not exist')
print(d)
"""

#5
"""
d = {1:'a',2:'b',3:'c',4:'d',3:'f'}
dic1={1:10, 2:20}
d2={}
for i in d,dic1:
    print(d2.update(i))
print(d2)
"""

#6
"""
n=5
d = {i:i*i for i in range(1,n+1)}
print(d)
"""

#7
"""
d= {i:i*i for i in range(1,16)}
print(d)
"""

#8
"""
a = {1:'a'}
b = {2:'b'}
c = b.update(a)
print(c)
"""

# 10 and 11 sum and multiply all the items in the dictionary
"""
dic1={1:10, 2:20}
dic1={i:i*i for i in dic1.values()}
print(dic1)
"""

#12 remove a key from dictionary
"""
d = {1:'a',2:'b',3:'c',4:'d',3:'f'}
del d[3]
print(d)
"""

#13 two lists into dictionary
"""
l1=[1,2,3,4,5]
l2=[9,8,7,6,0]
d1 = {i:j for i,j in zip(l1,l2)}
print(d1)
"""

#14 sort values by keys
"""
d = {5:'z',1:'a',2:'b',3:'c',4:'d',3:'f'}
d1 = (sorted(d.items()))
print(d1)
"""

# 15 get max and min values
d = {5:'z',1:'a',2:'b',3:'c',4:'d',3:'f'}
print("max values:- ", max(d.values()))
print("min values:- ", min(d.values()))