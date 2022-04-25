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
			
	def issorted(self):
		if self.head is None:
			return True
		
		temp = self.head
		while temp.next:
			if temp.data >= temp.next.data:
				return False
			temp = temp.next
		return True


ll = Linkedlist()
ll.begin(5)
ll.begin(4)
ll.begin(30)
ll.begin(2)
ll.begin(1)
ll.display()
print(ll.issorted())
