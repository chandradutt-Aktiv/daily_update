# '''

# filter map and reduce function
from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10]

fil_list = list(filter(lambda x: (x*2 > 10), l))
print(fil_list)
map_list = list(map(lambda x:x*2,l))
print(map_list)
reduce_list = reduce(lambda x, y:x+y,l)
print(reduce_list)


# Python local and global variables

x = 'global variable called'
def gl():
    x=2
    y='local variable'
    print('Inside fucntion ', x*2)
gl()
print('outside function', x)


# Python decorators

def shout(text):
    return text.upper()
print(shout('Hello'))

yell = shout
print(yell('world'))




def decor1(func):
    def inner():
        x = func()
        return x * x
def decor(func):
    def inner():
        x = func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10
print(num)



def f1():
    a=10
    b=9

    return [a,b]


print(f1())




# Recursive function

#tower of hanoi problem

def toh(n,source_pole, destination_pole, auxilary_pole):
    if(n==0):
        return

    toh(n-1,source_pole,auxilary_pole,destination_pole)
    print('Move the disk', source_pole, 'from', source_pole, 'to', destination_pole)
    toh(n-1,auxilary_pole,destination_pole,source_pole)

(toh(3,'S','D','A'))

# factorial program using recursion
def fact(n):
    if(n<=1):
        return 1
    return n*fact(n-1)

print(fact(5))


def fun1(n):
    if(n<1):
        return
    else:
        print(n)
        fun1(n-1)
        print(n)

fun1(3)

print('hello world %d python %s' % (1.,'programing'))
print('hello {} you are good at {}'.format('world','python'))

print(abs(1.1+2.2))