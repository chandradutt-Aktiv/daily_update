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
		
	def delete_without_head(self):
		temp = 2
		curr = self.head
		while curr.data != temp:
			curr = curr.next
			
		curr.data = curr.next.data
		curr.next = curr.next.next
		
		
	def display(self):
		if self.head == None:
			return 'list is empty'
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next


ll = Linkedlist()
ll.begin(1)
ll.end(2)
ll.end(3)
ll.end(4)
ll.delete_without_head()
ll.display()
