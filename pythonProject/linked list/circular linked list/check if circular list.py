class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	
class CircularList:
	def __init__(self):
		self.last = None
		
	def insert_empty(self, data):
		if self.last != None:
			return 'not empty list'
		newnode = Node(data)
		self.last = newnode
		self.last.next = self.last
		return self.last
	
	def begin(self, data):
		if self.last == None:
			return self.insert_empty(data)
		
		newnode = Node(data)
		newnode.next = self.last.next
		self.last.next = newnode
		
		return self.last
	
	def end(self, data):
		if self.last == None:
			return self.insert_empty(data)
		
		newnode = Node(data)
		newnode.next = self.last.next
		self.last.next = newnode
		self.last = newnode
		
		return self.last
	
	def display(self):
		if self.last == None:
			return 'list is None'
			
		temp = self.last.next
		while temp:
			print(temp.data)
			temp = temp.next
			if temp == self.last.next:
				break
	
	def is_circular(self):
		if self.last == None:
			return True
		else:
			temp = self.last
			while temp:
				if temp.next == self.last.next:
					return True
				temp = temp.next
		return False
	
cl = CircularList()
cl.insert_empty(6)
cl.begin(4)
cl.begin(2)
cl.end(8)
cl.end(12)
# cl.end(4)
# cl.end(5)
cl.display()
print(cl.is_circular())
