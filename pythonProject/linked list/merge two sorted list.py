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


def sortedMerge(head1, head2):
	# code here
	if head1 is None:
		return head2  # if head2 is None, then it returns an empty list
	elif head2 is None:
		return head1
	else:
		curr1 = head1
		curr2 = head2
		
		if curr1.data <= curr2.data:
			head = curr1
			curr = curr1
			curr1 = curr1.next
		else:
			head = curr2
			curr = curr2
			curr2 = curr2.next
		# head = curr1 if curr1.data <= curr2.data else curr2
		prev = curr
		while curr1 is not None and curr2 is not None:
			if curr1.data <= curr2.data:
				curr = curr1
				curr1 = curr1.next
			else:
				curr = curr2
				curr2 = curr2.next
			prev.next = curr
			prev = curr
		
		curr.next = curr2 if curr1 is None else curr1
		
		return head
	

l1 = Linkedlist()
l1.begin(15)
l1.begin(10)
l1.begin(5)
# print('list 1')
# l1.display()

# l1.head = mergelist()

l2 = Linkedlist()
# print('list 2')
l2.begin(20)
l2.begin(3)
l2.begin(2)

l1.head = sortedMerge(l1.head, l2.head)
l2.display()
