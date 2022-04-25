arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
s = 0
e = n-1
def reverse(arr, s, e):
	if s >= e:
		return
	
	arr[s], arr[e] = arr[e], arr[s]
	print(arr)
	reverse(arr, s+1, e-1)

reverse(arr, s, e)
