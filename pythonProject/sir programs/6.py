"""Write a program that accepts a sentence and calculate the number of
uppercase letters and lowercase letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

u=[]
l=[]
words = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


s = str(input('enter string: '))
for i in range(len(s)):
    if(s[i] in words):
        u.append(i)
    else:
        l.append(i)

print('upper ',len(u))
print('lower ',len(l))