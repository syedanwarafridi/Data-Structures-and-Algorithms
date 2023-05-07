class Node:
	def __init__(self, val):
		self.data = val
		self.next = None
		
		
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
		
	def PushINFront(self, val):
		newNode = Node(val)
		if self.head is None:
			self.head = newNode
			self.tail = newNode
		else:
			newNode.next = self.head
			self.head = newNode
		self.size += 1
		
	def PushINLast(self, val):
		newNode = Node(val)
		if self.tail is None:
			self.head = newnode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode
		self.size += 1
		
	def PushAfter(self, prevNode, val):
		newNode = Node(val)
		if prevNode is None:
			return
		newNode.next = prevNode.next
		prevNode.next = newNode
		if newNode.next is None:
			self.tail = newNode
		self.size += 1
		
	def removeFirst(self):
		if self.head is None:
			return None
		removeNode = self.head
		self.head = self.head.next
		if self.head is None:
			self.tail = None
		self.size -= 1
		return removeNode.data
		
	def removeLast(self):
		if self.tail is None:
			return None
		if self.head == self.tail:
			removeNode = self.head
			self.head = None
			self.tail = None
		else:
			currNode = self.head
			while currNode.next != self.tail:
				currNode = currNode.next
			removeNode = self.tail
			currNode.next = None
			self.tail = currNode
			
		self.size -= 1
		return removeNode.data
		
	def removeAfter(self, key):
		currNode = self.head
		prevNode = None
		while currNode.next is not None and currNode.data != key:
			prevNode = currNode
			currNode = currNode.next
		if currNode is None:
			return
		if prevNode is None:
			self.head = currNode.next
		else:
			prevNode.next = currNode.next
		if currNode.next is None:
			self.tail = prevNode.next
		self.size -= 1
		return currNode.data
		
	def is_empty(self):
		return self.head is None

	def __len__(self):
		return self.size
	
	def __iter__(self):
		current_node = self.head
		while current_node:
			yield current_node.data
			current_node = current_node.next
		
		
#### Main function

# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.PushINFront(3)
llist.PushINFront(2)
llist.PushINFront(1)
llist.PushINLast(4)
llist.PushINLast(5)

# print the contents of the linked list
print("Linked list contents:", end=" ")
for node in llist:
    print(node, end=" ")

# remove nodes from the linked list
llist.removeFirst()
llist.removeLast()
llist.removeAfter(2)

# print the contents of the linked list again
print("\nLinked list contents after removal:", end=" ")
for node in llist:
    print(node, end=" ")

