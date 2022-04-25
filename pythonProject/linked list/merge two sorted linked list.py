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


def mergelist(l1, l2):
	dummy = Node(0)
	tail = dummy

	while True:
		if l1 is None:
			tail.next = l2
			break
		if l2 is None:
			tail.next = l1
			break

		if l1.data <= l2.data:
			tail.next = l1
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next
		tail = tail.next
	return dummy.next

l3 = Linkedlist()

l1 = Linkedlist()
l1.begin(15)
l1.begin(10)
l1.begin(5)

l2 = Linkedlist()
l2.begin(20)
l2.begin(3)
l2.begin(2)

l1.head = mergelist(l1.head, l2.head)
l2.display()
