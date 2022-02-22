"""Write a program to print the below pattern
        *
      * *
    * * *
  * * * *
* * * * *

"""
j=1
for i in range(5,0,-1):
    print('-'*i,end='')
    print('*'*j,end=' ')
    j+=1
    print('\r')