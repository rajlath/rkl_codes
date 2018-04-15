class Nodes(object):
    def __init__(self, node_data, next_node=None):
        self.node_data = node_data
        self.next_node = next_node
        self.indx      = 0

class SLL(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def get_size(self):
        size = 0
        curr = self.head
        while curr != None:
            size += 1
            curr = curr.next_node
        return size


    def assign_index(self ):
        position = 0
        curr = self.head
        while curr != None:
            curr.indx = position
            position += 1
            curr = curr.next_node

    def add_node(self, data):
        '''
        inserts a node at the beginning
        '''
        new_node = Nodes(data)
        temp = self.head
        self.head = new_node
        if temp != None:
            self.head.next_node = temp

    def append_node(self, data):
        '''
        adds a node at the end
        '''
        new_node = Nodes(data)
        curr = self.head
        if curr == None:self.add_node(data)
        else:
            while curr.next_node != None:
                curr = curr.next_node
            curr.next_node = new_node

    def insert_node(self, data, position):
        if position == 0:
            self.add_node(data)
        elif position > self.get_size():
            self.append_node(data)
        else:
            new_node = Nodes(data)
            curr = self.head
            self.assign_index()
            previous = None
            curr_pos = 0
            while curr_pos != position:
                previous = curr
                curr     = curr.next_node
                curr_pos += 1
            previous.next=new_node
            new_node.next=curr.next_node
        self.assign_index()


    def __str__(self):
        self.assign_index()
        curr = self.head
        while curr != None:
            print("{}:{}".format(curr.indx, curr.node_data), end= ",")
            curr = curr.next_node
        return ""


sll = SLL()
sll.add_node(12)
sll.add_node(24)
sll.add_node(36)
sll.append_node(48)
sll.insert_node(52,0)
sll.insert_node(23, 12)
sll.insert_node(28, 4)
print(sll)
print(sll.get_size())























