class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

class CircularList:
	def __init__(self):
		self.head = None
	
	def push(self, data):
		newnode = Node(data)
		temp = self.head
		newnode.next = self.head
		if self.head is not None:
			while temp.next != self.head:
				temp = temp.next
			temp.next = newnode
		else:
			newnode.next = newnode
		self.head = newnode
		
	def display(self):
		temp = self.head
		if self.head is not None:
			while True:
				print(temp.data)
				temp = temp.next
				if temp == self.head:
					break
					
cl = CircularList()
cl.push(1)
cl.push(2)
cl.push(3)
cl.push(4)
cl.push(5)
cl.display()
