"""Write a program to generate below Pattern:
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
"""
j=1
for i in range(6,0,-1):
    print(' '*i,end=' ')
    print('* '*j,end=' ')
    j+=1
    print('\r')