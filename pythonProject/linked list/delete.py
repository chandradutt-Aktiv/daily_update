class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

class Linkedlist:
	"""
	list
	"""
	def __init__(self):
		self.head = None
		
	def search_element(self, element):
		"""
		search element
		"""
		temp = self.head
		if self.head is None:
			print('No elements')
		
		while temp:
			if temp.data == element:
				print('element', temp.data)
				print('element found')
				# temp = temp.next
				return
			# else:
			# 	print('No element', temp.data)
			# 	print('not found')
				# temp = temp.next
			temp = temp.next
			
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
		print('deleted')
	
	def dellist(self):
		"""
			delete all data into linked list
		"""
		temp = self.head
		while temp:
			prev = temp.next
			del temp.data
			temp = prev
		print('list deleted')
		
	def delend(self):
		"""

		"""
		temp = self.head
		while temp:
			temp = temp.next
			del temp.data
		print(temp, 'deleted')
		
	def disp(self):
		"""
		display data
		"""
		temp = self.head
		# if self.head is None:
		# 	print('no data in list')
		# else:
		# 	pass
		
		while temp:
			print(temp.data)
			temp = temp.next
		
			

ll = Linkedlist()
ll.insertbeg(1)
ll.insertbeg(2)
ll.disp()
# ll.delbegin()
ll.insertbeg(4)
ll.insertbeg(3)
ll.disp()
ll.search_element(40)
# ll.dellist()
ll.disp()
