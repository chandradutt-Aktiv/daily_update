#git token - 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



'''
from collections import Counter
l1 = [19, 19, 15, 5, 3,5,5, 2]
res = l1.count(19)==2 and l1.count(5>=3)
print(res)

count={}
s1=set(l1)

d1={}
for j in s1:
    for i in l1:
        d1[i]=(l1.count(i))

print(d1)

for i in d1:
    if(d1[19]==2 and d1[5]>=3):
        print(True)
    else:
        print(False)


def a(l1):
    s1 = set(l1)
    d1={}
    for i in l1:
        for j in s1:
            d1[i]=l1.count(i)
    print(d1)
    l = len(l1)
    for i in l1:
        if (l == 8 and d1[5] >= 3):
            return True
        else:
            return False


l1 = [19, 15, 11, 7, 5, 6, 2]
print(a(l1))



n = 854

if(n > 4*4*4*4 and (n%34)==4):
    print(True)
else:
    print(False)



n = 17
l1=[]
for i in range(n):
    l1.append(n)
    n += 2

print(l1)



l1 = ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
n = len(l1)
print(n)

if(l1[n-2] in l1[n-1]):
    print(True)
else:
    print(False)



l1=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]
l2=[]
for i in range(len(l1)-1):
    if(l1[i+1]-l1[i] == 10):
        l2.append(True)
    else:
        l2.append(False)

if(True in l2):
    print(True)
else:
    print(False)





l1 = [2, 2, 2, 2, 2]
n = len(l1)
s = sum(l1)
print(s)
if(s == n):
    print(True)
else:
    print(False)




string = 'W3resource Python, Exercises.'

s1=string.replace(",","")
s2=s1.split(" ")
print(s2)
l = []
for i in string:
    if(i == " " or i == ',' and i == ', ' ):
        l.append(i)

print(l)
fl=[]
fl.append(s2)
fl.append(l)
print(fl)






def aa(l):
    return all([l[i] != l[i+1] for i in range(len(l)-1)]) and len(set(l))==4

l = [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
print(aa(l))

l = set(l)
print(l)




str = '( ()) ((()()())) (()) ()'
str2=''
l1=[]
count = 0
str = str.replace(" ","")
print(str)
for i in str:
    if(i == '('):
        count += 1
        str2 = str2+i
    if(i == ')'):
        count -= 1
        str2 = str2+i

    if(count == 0):
        l1.append(str2)
        str2=""
print(l1)






l = [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
l1 = []
for i in l:
    print(i[0],i[1])
    for j in i[1]:
        if(i[0] > j):
            l1.append(j)
            print(i[1])

print(l1)
print(list(enumerate(l,i)))




l1 = ['palindrome', 'madamimadam', '', 'foo', 'eyes']

for i in l1:
    if(i == i[::-1]):
        print(True)
    else:
        print(False)





#14
l1 = [ 'ca',('cat', 'cr', 'fear', 'canter')]
s1 = []
prefix = 'ca'

for i in range(len(l1[1])):
    if(l1[0] in l1[1][i]):
        print(l1[1][i])

'''
#15
"""def f():
    return max(l2,key=len)

l2 = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print(f())
"""
#16
"""
l = [('cat', 'car', 'fear', 'center')]
ch = 'ca'

for i in l[0]:
    if(ch in i):
        print(i)

"""


#17
"""
n = 15
for i in range(0,n+1):
    print(str(i), end=" ")

"""
#18
"""
l = ([1, 3, 2, 32, 19],
     [19, 2, 48, 19],
     [],
     [9, 35, 4],
     [3, 19])
v = 19
l1=[[i,j] for i,r in enumerate(l) for j,x in enumerate(r) if v == x]
print(l1)

for i,r in enumerate(l):
    for j,x in enumerate(r):
        if(v==x):
            print(i,j)
"""


#20
"""
l = [6, 5, 4, 3, 2, 1]
def inc(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if(l[i] > l[j]):
                return 'increasing'
            elif(l[i] < l[j]):
                return 'decreasing'
        else:
            return 'non monotonic'

print(inc(l))
"""

#21
"""
l = ['ca t', 'car', 'fea r', 'cente r']

l1 = [len(i.split(' ')[-1])==1 for i in l]
print(l1)

for i in l:
    print(i)
    if(' ' in i):
        print(True)
    else:
        print(False)
        
        
"""


# 22
"""
st = "SUNNY"
l=[]
for i in st:
    if(i.isupper()):
        l.append(ord(i))

print(sum(l))
"""


#23
"""
l = [6, 5, 4, 3, 2, 1]
nl = []
for i in range(len(l)):
    if(l[i]<l[i-1]):
        nl.append(i)

print(nl)

"""


#24
"""
l = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
nl=[max(l[:i]) for i in range(1, len(l)+1) ]
print(nl)


def test(nums):
    return [max(nums[:i+1]) for i in range(len(nums))]

nums = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
print(test(nums))

"""

#74
"""
d1 =  {'f': 1, 'o': 2,'c':5}
d = [key * val for key,val in d1.items()]
print(d)

"""


#25
"""
l = ['100011101100001', '100101100101110']
#bin() is used to convert integer to binary number
l1 = [bin(int(l[0],2) ^ int(l[1],2))]
print(l1)
"""


#26
"""
l = ['100', '102,1', '101.1','199,9']

l1 = [max(float(i.replace(",","."))for i in l)]
print(l1)

for i in l:
    if(',' in i):
        i = i.replace(',','.')
        print(i)

"""

#27
"""
l=[4, -5, 17, -9, 14, 108, -9]
n = len(l)
s = sum(l)
mean = s/n
print(mean)"""


#28
l=['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']

l1=[lambda x:len(set(i)) for i in l]
print(list(l1))

l = max(l, key=lambda x:len(set(x)))
print(l)


