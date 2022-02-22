"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit
as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
"""

n = 8
n1=str(n)*1
n2=str(n)*2
n3=str(n)*3
n4=str(n)*4

sum = int(n1) + int(n2) + int(n3) + int(n4)
print(sum)
