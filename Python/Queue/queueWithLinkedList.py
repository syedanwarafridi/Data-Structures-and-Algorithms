class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
        def __init__(self):
            self.front = None
            self.rear = None
            self.size = 0

        def isEmpty(self):
            return self.front is None

        def enQueue(self, val):
            newNode = Node(val)
            if self.rear is None:
                self.front = newNode
                self.rear = newNode
            else:
                self.rear.next = newNode
                self.rear = newNode

            self.size += 1

        def deQueue(self):
            if self.front is None:
                return None
            deququeNode = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.size -= 1
            return deququeNode.data

        def Peek(self):
            if self.front is None:
                return None
            return self.front.data
        
        def __len__(self):
            return self.size

# create a new queue
queue = Queue()

# enqueue some items
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)

# get the size of the queue
print("Queue size: ", len(queue))

# get the front item of the queue
print("Front item: ", queue.Peek())

# dequeue an item from the queue
dequeued_item = queue.deQueue()
print("Dequeued item: ", dequeued_item)

# check if the queue is empty
print("Is queue empty? ", queue.isEmpty())
