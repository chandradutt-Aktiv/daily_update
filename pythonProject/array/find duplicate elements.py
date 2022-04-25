import time
start = time.time()
arr = [0, 4, 3, 2, 7, 8, 2, 3, 1]
n = len(arr)

# for i in range(n):
# 	x = arr[i] % n
# 	arr[x] += n
#
# for i in range(n):
# 	if arr[i] >= n*2:
# 		print(i)
# print(arr.count(arr))

dup = {i: arr.count(i) for i in arr}

for i, j in dup.items():
	if j > 1:
		print(i)
count = {}
end = time.time()

print('time consumed ', end-start)
# for i in arr:
# 	if i not in count:
# 		count[i] = 1
# 	else:
# 		count[i] += 1
# print(count)
