"""Write a program that computes the net amount of a bank account based
a transaction log from console input. The transaction log format is
shown as following:
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
D means deposit while W means withdrawal.
Then, the output should be:
500
"""

total = 0
while True:
    s = input('enter tranjection type and amount: ')
    if not s:
        break
    values = s.split(" ")
    tranjection = values[0]
    amount = values[1]

    if(tranjection == "D"):
        total += int(amount)
    elif(tranjection == "W"):
        total -= int(amount)
    else:
        pass
print('Total amount is: ',total)