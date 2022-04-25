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
		
	def end(self, data):
		newnode = Node(data)
		if self.head == None:
			self.head = newnode
		
		temp = self.head
		while temp.next:
			temp = temp.next
		temp.next = newnode
		
	def display(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
			
	def delete_common_unsorted(self):
		curr = self.head
		prev = Node(None)
		mset = set()
		while curr:
			val = curr.data
			if val in mset:
				prev.next = curr.next
			else:
				mset.add(val)
				prev = curr
			curr = curr.next
		return curr
		
ll = LinkedList()
ll.begin(1)
ll.end(2)
ll.end(5)
ll.end(3)
ll.end(7)
ll.end(2)
ll.end(3)
ll.delete_common_unsorted()
ll.display()