class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	
class CircularList:
	def __init__(self):
		self.last = None
		
	def insert_empty(self, data):
		if self.last != None:
			return
		newnode = Node(data)
		self.last = newnode
		self.last.next = self.last
		return self.last
	
	def begin(self, data):
		if self.last == None:
			return self.insert_empty(data)
		newnode = Node(data)
		newnode.next = self.last
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
	
	def position(self, data, pos):
		if self.last == None:
			return None
		
		newnode = Node(data)
		temp = self.last.next
		while temp:
			# temp = temp.next
			if temp.data == pos:
				newnode.next = temp.next
				temp.next = newnode
				
				if temp == self.last:
					self.last = temp
					return self.last
				else:
					return self.last
				
			temp = temp.next
			if temp == self.last.next:
				print('element not in list')
				break
	
	def display(self):
		temp = self.last.next
		while temp:
			print(temp.data)
			temp = temp.next
			if temp == self.last.next:
				break
		
		
cl = CircularList()
cl.begin(1)
cl.end(2)
cl.end(3)
cl.end(4)
cl.end(5)
cl.position(100, 3)
cl.display()
