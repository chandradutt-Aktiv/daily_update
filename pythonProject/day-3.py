'''ab = {'swaroop':'abc@gmail.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

print(ab['swaroop'])
del ab['Larry']
print(ab)
print('there are contacts {} in the address book'.format(len(ab)))
print('in the dictionary key is: {} and values are: {}'.format(ab.keys(), ab.values()))

for name, address in ab.items():
    print('contacts {} at {}'.format(name, address))

ab['hello'] = 'world'
print(ab)

ab[7]=8
ab.update(z='asd')
print(ab)

l1=[1,2,3]
l2=[4,5,6]
l1.insert(2,10)
l1.extend(l2)
str = 'hello'
x=str.join(['a','v','d'])
print(x)
print(l1)

'''

l1 = [1,2,3,4]
for i in zip(l1):
    print(dict(i))
print(enumerate(l1))
print(ascii(l1))
x=complex(3+4j)
print((x))
