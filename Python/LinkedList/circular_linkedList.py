class Node:
	def __init__(self, val):
		self.data = val
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def isEmpty(self):
		return self.head is None

	def len(self):
		return self.size

	def __iter__(self):
		currNode = self.head
		while currNode:
			yield currNode.data
			if currNode.next == self.head:
				break
			currNode = currNode.next

	def Append(self, val):
		newNode = Node(val)
		if self.isEmpty():
			self.head = newNode
			self.tail = newNode
			self.tail.next = self.head

		else:
			self.tail.next = newNode
			self.tail = newNode
			self.tail.next = self.head
		self.size += 1

	def Prepend(self, val):
		newNode = Node(val)
		if self.isEmpty():
			self.head = newNode
			self.tail = newNode
			self.tail.next = self.head

		else:
			newNode.next = self.head
			self.head = newNode
			self.tail.next = self.head
		self.size += 1

	def Remove(self, key):
		if self.isEmpty():
			return
		if self.head.data == key:
			if self.head == self.tail:
				self.head = None
				self.tail = None
			else:
				self.head = self.head.next
				self.tail.next = self.head
			self.size -= 1
			return
		currNode = self.head
		while currNode.next != self.head:
			if currNode.next.data == key:
				if currNode.next == self.tail:
					self.tail = currNode
					self.tail.next = self.head
				else:
					currNode.next = currNode.next.next
				self.size -=  1
				return
			currNode = currNode.next
		return

	def print_list(self):
		if self.size == 0:
			print("Circular linked list is empty")
			return
		current_node = self.head
		while current_node.next != self.head:
			print(current_node.data, end=" -> ")
			current_node = current_node.next
		print(current_node.data, end=" -> ")
		print("\n")

if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.Prepend(5)
    cll.Prepend(4)
    cll.Append(6)
    cll.Append(7)
    cll.Remove(5)
    cll.print_list()
