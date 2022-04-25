import os
import sys

print(os.getcwd())

print(os.name)
print(sys.version)
a = 'chandradutt patel'
print(sys.getrefcount(a))

# dictionary comprehension

keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
dict1 = {i: j for i, j in zip(keys, values)}
print(dict1)

dict2 = {i: i * 2 for i in range(1, 11) if (i % 2 == 0)}
print(dict2)

words = ['data', 'science', 'machine', 'learning']
values = [5, 3, 1, 8]
l = [len(i) if (len(i) > 5) else 'short' for i in words]
print(l)
d = {i: len(i) if (len(i) > 5) else 'short' for i in words}
print(d)
d1 = {i: j if (j > 3) else 'less value' for i, j in zip(words, values)}
print(d1)

lst = ['data', 'science', 'artificial', 'intelligence']
dct = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}

dct1 = {i: dct[i] if (i in dct) else len(i) for i in lst}
print(dct1)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

dict3 = {(i, j): i * j for i, j in zip(l1, l2)}
print(dict3, end="\r")

# Lambda with filter

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

fl = list(filter(lambda x: (x % 2 != 0), li))
print(fl)

m = map(lambda x: x ^ 2, li)
print(list(m))

# Exception Handling

a = [1, 2, 3]

try:
	print('second element = %d' % (a[1]))
	
	print('printing 4th position = %d' % (a[4]))

except:
	print('error')


def fun(a):
	if (a < 4):
		b = a / (a - 3)
		print(b)


try:
	fun(3)
	fun(5)
except ZeroDivisionError:
	print('zero division error handled')
else:
	print('runned')
finally:
	print('code runned successfully')
