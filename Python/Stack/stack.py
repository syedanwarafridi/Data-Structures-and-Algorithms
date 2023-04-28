class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return len(self.items) == 0
	
	def Push(self, item):
		self.items.append(item)
		
	def Pop(self):
		if not self.isEmpty():
			return self.items.pop()
	
	def size(self):
		return len(self.items)
		
	def Peek(self):
		if not self.isEmpty():
			return self.items[-1]
	

# Main Fucntion
stack = Stack()

stack.Push(1)
stack.Push(2)
stack.Push(3)

print("Stack Size is: ", stack.size())

print("Stack Peek is: ", stack.Peek())

poppedItem = stack.Pop()
print("Popped Item is: ", poppedItem)

print("Is Stack Empty? ", stack.isEmpty())
