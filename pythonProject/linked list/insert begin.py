"""
insert node at begin in linked list
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	
	
class begin:
	"""
	insert node at begin in linked list
	"""
	def __init__(self):
		self.head = None
		
	def insertbeg(self, data):
		"""
		insert node at begin in linked list
		"""
		newnode = Node(data)
		newnode.next = self.head
		self.head = newnode
		print('inserted')
	
	def delbegin(self):
		if self.head is None:
			return
		
		self.head = self.head.next
		print('deletedd')
		
	def insertpos(self, data, pos):
		newnode = Node(data)
		if self.head is None:
			self.head = newnode
			return
		
		temp = self.head
		while temp:
			if temp == pos:
				temp.next = newnode
				newnode.next = temp.next.next
			temp = temp.next
			
		
	def insertend(self, data):
		newnode = Node(data)
		
		# newnode = self.head
		if self.head is None:
			self.head = newnode
			return
		
		temp = self.head
		while temp.next:
			# if(temp.next == None):
			temp = temp.next
		temp.next = newnode
		print('exitedd')
				
	def display(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
	
	def search(self, key):
		temp = self.head
		
		while temp:
			if(temp.data == key):
				print('element found')
				return
			else:
				temp = temp.next
			
ll = begin()
ll.insertbeg(1)
ll.display()
ll.delbegin()
ll.insertbeg(2)
ll.insertbeg(23)
ll.insertend(50)
ll.insertpos(60, 1)
ll.display()
ll.search(2)
