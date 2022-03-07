# Python program to check if the number is an Armstrong number or not

# take input from the user

"""
armstrong number program and check the number is
armstrong or not
"""
num = int(input("Enter a number: "))

sum1 = 0

temp = num
while temp > 0:
	digit = temp % 10
	sum1 += digit ** 3
	temp //= 10

if num == sum1:
	print(num, "is an Armstrong number")
else:
	print(num, "is not an Armstrong number")
