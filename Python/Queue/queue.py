class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
            return len(self.items) == 0
    
    def enQueue(self, val):
            self.items.append(val)

    def deQueue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)
    
    def Peek(self):
        return self.items[0] if not self.isEmpty() else None

    def Size(self):
        return len(self.items)

queue = Queue()

# enqueue some items
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)

# get the size of the queue
print("Queue size: ", queue.Size())

# get the front item of the queue
print("Front item: ", queue.Peek())

# dequeue an item from the queue
dequeued_item = queue.deQueue()
print("Dequeued item: ", dequeued_item)

# check if the queue is empty
print("Is queue empty? ", queue.isEmpty())