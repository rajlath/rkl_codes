class Node:
    def __init__(self,data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return self.data

    def set_next(self, nexts)    :
        self.next = nexts

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def set_prev(self, prevs):
        self.prev =   prevs

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev != None

    def __str__(self):
        return "Node Data is  {}".format(self.data)

class DLL:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length

    def insert_at_start(self, data)    :
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.set_pre = None
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            self.head = new_node

    def add_to_the_last(self, data):
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            curr = self.head
            while curr.get_next() != None:
                curr = curr.get_next()
            curr.set_next(new_node)
            self.tail = curr.get_next()

    def delete_at_start(self):
        curr = self.head
        if curr is None:return
        self.head = curr.next
        self.head.prev = None
        self.length -= 1

    def delete_at_end(self)    :
        curr = self.head
        if curr is None:return
        while curr.next != None:
            prev = curr
            curr = curr.next
        self.tail = prev
        self.length -= 1

    def delete_at_pos(self, pos):
        curr = self.head
        if curr is None:return
        indx = 0
        while curr.next != None:
            prev = curr.prev
            if indx == pos:
                curr = curr.get_next()
                curr.set_prev(prev)
                self.length -= 1
                return
            else:
                curr = curr.get_next
        indx += 1


    def delete_value(self, value)        :
        curr = self.head
        prev = None
        while curr is not None:
            prev = curr.get_prev
            if curr.get_data() == value:
                if curr.get_next() is not None:
                    prev.set_next(curr.get_next)
                else:
                    prev.set_next(None)
            curr = curr.next

    def print(self)         :
       curr = self.head
       while curr is not None:
           print(curr.data, end = " ")
           curr = curr.next

dll = DLL()
dll.insert_at_start(12)
dll.add_to_the_last(32)
dll.add_to_the_last(132)
dll.add_to_the_last(78)
dll.print()
dll.delete_at_pos(1)
dll.print()

















