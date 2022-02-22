"""Write a program to generate below Pattern:
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""
j=6
for i in range(0,6):
    print(' '*i,end='')
    print('* '*j, end=' ')
    j-=1
    print('\r')