class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

class Linkedlist:
	def __init__(self):
		self.head = None
		
	def end(self, data):
		newnode = Node(data)
		if self.head is None:
			self.head = newnode
			return
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = newnode
	
	def display(self):
		temp = self.head
		
		while temp:
			print(temp.data)
			temp = temp.next
			
	def last_to_first(self):
		temp = self.head
		prev = None
		while temp and temp.next:
			prev = temp
			temp = temp.next
		
		prev.next = None
		temp.next = self.head
		self.head = temp
		

ll = Linkedlist()
ll.end(1)
ll.end(2)
ll.end(3)
ll.end(4)
ll.end(5)
ll.last_to_first()
ll.display()