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
		if self.last == None:
			return self.insert_empty(data)
		
		newnode = Node(data)
		newnode.next = self.last.next
		self.last.next = newnode
		return self.last
	
	def count(self):
		c = 0
		temp = self.last.next
		while temp:
			c += 1
			print(temp.data)
			temp = temp.next
			if temp == self.last.next:
				print('length of list', c)
				break
			
			
cl = CircularList()
cl.begin(1)
cl.begin(2)
cl.begin(3)
cl.begin(4)
cl.count()
