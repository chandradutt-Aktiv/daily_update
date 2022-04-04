class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def begin(self, data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode
		
	def end(self, data):
		newnode = Node(data)
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = newnode
		
	def display(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
			
	def nth(self, n):
		count = 0
		temp = self.head
		while temp:
			if n == count:
				print('nth node found from begin', n, temp.data)
				return
			else:
				temp = temp.next
				count += 1
				
	def endn(self, n):
		count = 0
		temp = self.head
		while temp:
			count += 1
			temp = temp.next
		
		print('count', count)
		aa = count - n
		print('aa', aa)
		
		if n > count:
			print('lsadklasdfkj', -1)
		prev = self.head
		c1 = 0
		while prev:
			if c1 == aa:
				print('zz', prev.data)
			c1 += 1
			prev = prev.next
		
ll = LinkedList()
ll.begin(623)
ll.end(84)
ll.end(954)
ll.end(756)
ll.end(840)
ll.end(966)
ll.end(376)
ll.end(931)
ll.end(308)
ll.display()
ll.nth(4)
ll.endn(10)
