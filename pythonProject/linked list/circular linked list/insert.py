class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
class CircularList:
	def __init__(self):
		self.last = None
		
	def insert_empty(self, data):
		if self.last != None:
			return self.last
		
		newnode = Node(data)
		self.last = newnode
		self.last.next = self.last
		return self.last
		
	def begin(self, data):
		newnode = Node(data)
		if self.last == None:
			return self.insert_empty(data)
		newnode.next = self.last.next
		self.last.next = newnode
		return self.last
	
	def end(self, data):
		if self.last == None:
			return self.insert_empty(data)
		newnode = Node(data)
		newnode.next = self.last.next
		self.last.next = newnode
		self.last = self.last.next
		return self.last
	
	def insert_after(self, data, p):
		if self.last == None:
			return None
		newnode = Node(data)
		temp = self.last.next
		while temp:
			if temp.data == p:
				newnode.next = temp.next
				temp.next = newnode
				if temp == self.last:
					self.last = newnode
					return self.last
				else:
					return self.last
			temp = temp.next
			if temp == self.last.next:
				print('item not in list')
				break
	
	def display(self):
		if self.last == None:
			return 'list is empty'
		temp = self.last.next
		while temp:
			print(temp.data)
			temp = temp.next
			
			if temp == self.last.next:
				break


cl = CircularList()
cl.begin(1)
cl.begin(2)
cl.end(3)
cl.end(3)
cl.end(4)
cl.end(6)
cl.insert_after(10, 3)
cl.display()
