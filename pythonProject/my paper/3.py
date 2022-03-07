"""
Third program of paper
"""
# l=[i for i in range(1000, 10000):]

l = [1567, 3457, 7583, 1273, 7894, 3245, 2500]

for i in l:
	second = ((i % 1000) // 100)
	last = i % 10
	
	if second % 2 != 0 and last % 2 == 0:
		if i % 8 == 0 or i % 5 == 0:
			print(i)
