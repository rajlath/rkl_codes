class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data

class SLL(object):
    def __init__(self):
        self.llist = []
        self.head  = None
        self.tail  = None


    def add_to_head(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            return self
        else:
            node = self.head
            new_node = Node(data)
            self.head = new_node
            self.head.next = node
        return self
    def add_to_tail(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            self.tail = node
            return self
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
        return self
    def delete_node(self, data):
        if self.head == None:
            return self.head
        else:
            curr = self.head
            if curr.data == data:
                return self.head.next
            while curr.next != None:
                if curr.next.data == data:
                    curr.next = curr.next.next
                    return self.head
                curr = curr.next
        return self.head

    def print_sll(self):
        curr = self.head
        if curr == None:
            return ''
        else:
            print(curr.data, end=" ")
            while curr.next != None:
                print(curr.data, end=" ")
                curr = curr.next





sll = SLL()
sll.add_to_head(5)
sll.add_to_tail(6)
sll.print_sll()
sll.add_to_head(12)
sll.add_to_tail(8)







