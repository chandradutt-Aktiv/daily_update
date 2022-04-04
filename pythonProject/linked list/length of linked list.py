class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

class Linkedlist:
	def __init__(self):
		self.head = None
		
	def begin(self, data):
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode
		
	def display(self):
		temp = self.head
		count = 0
		while temp:
			count += 1
			print(temp.data)
			temp = temp.next
		print('numbers of nodes', count)
		


ll = Linkedlist()
ll.begin(1)
ll.begin(2)
ll.begin(3)
ll.begin(4)
ll.display()