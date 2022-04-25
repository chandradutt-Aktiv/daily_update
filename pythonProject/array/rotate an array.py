def rotate(arr, n):
	temp = arr[0]
	for i in range(n - 1):
		arr[i] = arr[i + 1]
	print(arr)
	arr[n - 1] = temp
	print(arr)


def rotateArr(A, D, N):
	# D %= N
	# print(2 %= 6)
	# First reversing d elements from starting index.
	A[0:D] = reversed(A[0:D])
	print(A)
	# Then reversing the last n-d elements.
	A[D:N] = reversed(A[D:N])
	print(A)
	# Finally, reversing the whole array.
	A[0:N] = reversed(A[0:N])
	print(A)

def times(arr, n, d):
	
	for i in range(d):
		rotate(arr, n)


A = [10, 20, 30, 40, 50, 60, 70]
N = len(A)
D = 5
print(rotateArr(A, D, N))
