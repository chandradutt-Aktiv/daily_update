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
		while temp:
			print(temp.data)
			temp = temp.next
	
	def zeros(self):
		temp = self.head
		prev = temp
		if self.head is None:
			return "Empty Linked list"
		
		while temp:
			if temp.data == 0:
				# print('zero', temp.data)
				curr = temp
				temp = temp.next
				prev.next = temp
				
				curr.next = self.head
				self.head = curr
			else:
				prev = temp
				temp = temp.next
				
			# temp = temp.next
			

ll = Linkedlist()
ll.begin(5)
ll.begin(4)
ll.begin(0)
ll.begin(0)
ll.begin(3)
ll.begin(2)
ll.begin(1)
ll.display()
ll.zeros()
print('&&&&&&&&&&&&&&&&&&&&&&&&&&')
ll.display()
