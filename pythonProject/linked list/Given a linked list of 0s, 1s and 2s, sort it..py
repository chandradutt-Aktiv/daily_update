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
		
	def end(self, data):
		newnode = Node(data)
		if self.head == None:
			self.head = newnode
		temp = self.head
		while temp.next:
			temp = temp.next
			
		temp.next = newnode
		newnode.next = None
		
	def sort_list(self):
		count = [0, 0, 0]
		temp = self.head
		while temp != None:
			count[temp.data] += 1
			temp = temp.next
		i = 0
		temp = self.head
		while temp != None:
			if count[i] == 0:
				i += 1
			else:
				temp.data = i
				count[i] -= 1
				temp = temp.next
			
	def display(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
	
ll = Linkedlist()
ll.begin(1)
ll.end(0)
ll.end(2)
ll.end(1)
ll.end(0)
ll.end(0)
ll.end(2)
ll.end(1)
ll.sort_list()
ll.display()