class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertFirst(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1

    def insertLast(self, val):
        newNode = Node(val)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def removeFirst(self):
        if self.head is None:
            return None
        removeNode = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return removeNode.data

    def removeLast(self):
        if self.tail is None:
            return None
        removeNode = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.size -= 1
        return removeNode.data

    def removeNode(self, node):
        if node is None:
            return
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1
        return node.data

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insertFirst(2)
    linked_list.insertLast(3)
    print("Linked list contents:")
    for node in linked_list:
        print(node)
