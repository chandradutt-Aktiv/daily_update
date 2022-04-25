a = lambda x: x * x
print(a(5))

print('hello : %2d, world : %5.2f' % (1000, 534.6709))
# print octal value
print('%2.3o' % 25) \
	 \
	# print exponential value
print('%5.3e' % (356.08977))

# .format method using different types of variables
print('Number one portal is {0:2d}, {1:2.3f}, and {other}.'.format(123, 45.6132, other='abcd'))

# format method using dictionary
dict1 = {'abc': 'hello', 'xyz': 'world'}
print(type(dict1))
print('hello world {abc} {xyz} ', format(**dict1))

# string io operation and print functions
import io

dmf = io.StringIO()
print('hello world', file=dmf)
dmf.getvalue()
print('a', 'b', 'c', sep='', end='#')

# Arithmatic operators
a = -5
print(+a)
b = 2
print(a % b)
# floor division
print('a//b= ', a // b)
print(31 / 4)
print(10 // -4)
print(-10 // -4)
print(31 // 4)

print(a * 25 + b)

#   **  exponential operator
#  power of two value
# print(a**b)


# bitwise operators

print('0b{:0b}'.format(0b1001 & 0b1101))
print('0b{:0b}'.format(0b1001 | 0b1101))
print('0b{:0b}'.format(0b1001 ^ 0b1101))
print('0b{:0b}'.format(0b101001 >> 2))
print('0b{:0b}'.format(0b1001 << 4))

# list comprehension
x = [i for i in range(20) if i % 2 != 0]
print(x)

mat = [[j for j in range(3)] for i in range(5)]
print(mat)

mul = list(map(lambda i: i * 10, [i for i in range(1, 11)]))
print(mul)

sq = [i ** 2 for i in range(10) if i % 2 == 0]
print(sq)

sq1 = list(map(lambda i: i ** 2, [i for i in range(10) if (i % 2 == 0)]))
print(sq1)

f = list(filter(lambda i: i % 2 == 0, [i for i in range(10)]))
print(f)

l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
l1 = []
tra = [[j[i] for i in range(len(l))] for j in l]
print(tra)
for i in range(len(l)):
	l2 = []
	for j in l:
		l2.append(j[i])
	l1.append(l2)
print(l1)

string = 'HeLlo worLd'
string = list(string)
print(string)
for i in string:
	if (i == 'e' and 'e' in string):
		print(str(i).upper())
string = str(string)
print(str(string))
print(string.upper())
