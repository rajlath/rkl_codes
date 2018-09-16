class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data)    :
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def dequeue(self):
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1

    def __str__(self)        :
        items = []
        curr = self.head
        while curr:
            items.append(curr.data)
            curr = curr.next
        return " ".join(map(str, items))


q = Queue()
q.enqueue(12)
q.enqueue(36)
q.enqueue(41)
print(q)
q.dequeue()
print(q)


