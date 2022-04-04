# def star(n):
# 	for i in range(n):
# 		for j in range(0, i + 1):
# 			print("*", end="")
#
# 		for k in range(n-1, i, -1):
# 			print(" ", end=" ")
#
# 		for j in range(0, i + 1):
# 			print("*", end="")
# 		print('\n', end="")
#
# 	for i in range(n-1, -1, -1):
# 		for j in range(0, i+1):
# 			print("*", end="")
#
# 		for k in range(n - 1, i, -1):
# 			print(" ", end=" ")
#
# 		for j in range(-1, i):
# 			print("*", end="")
# 		print('\n', end="")
#
#
# # for j in range(n, 0, -1):
# # 	print('*'*j)
#
#
# star(4)



def s1(n):
	for i in range(n):
		for j in range(0, i):
			if j % 2 == 0:
				print('1', end=' ')
			else:
				print('0', end=' ')
			# print(j, end=' ')
		print('\n', end=' ')
	
s1(5)