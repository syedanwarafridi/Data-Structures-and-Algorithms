class Node:
	
	def __init__(self, val=None):
		self.data = val
		self.next = None

class Stack:
	
	def __init__(self):
		self.top = None
		self.size = 0
		
	def Push(self, val):
		newNode = Node(val)
		newNode.next = self.top
		self.top = newNode
		self.size += 1
		
	def isEmpty(self):
		return self.top is None
		
	def Pop(self):
		if self.isEmpty():
			return None
		poppedNode = self.top
		self.top = poppedNode.next
		poppedNode.next = None
		self.size -= 1
		return poppedNode.data
		
	def Size(self):
		return self.size
		
	def Peek(self):
		return self.top.data if self.top else None
		
		
#Main Function
# create a new stack
stack = Stack()

# push some items onto the stack
stack.Push(1)
stack.Push(2)
stack.Push(3)

# get the size of the stack
print("Stack size: ", stack.Size())

# get the top item of the stack
print("Top item: ", stack.Peek())

# pop an item from the stack
popped_item = stack.Pop()
print("Popped item: ", popped_item)

# check if the stack is empty
print("Is stack empty? ", stack.isEmpty())

