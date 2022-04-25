class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		

class LinkedList:
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
			
	def reverse(self):
		curr = self.head
		prev = None
		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		return self.head
		
	
ll = LinkedList()
ll.begin(4)
ll.begin(3)
ll.begin(2)
ll.begin(1)
# ll.display()
ll.reverse()
ll.display()
