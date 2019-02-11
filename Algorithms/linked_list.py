class Node:
    def __init__(self, data=None, next=None):
        self.data = None
        self.next = None
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self, nxt):
        self.next = nxt
    def get_next(self):
        return self.next
    def has_next(self):
        return self.next != None

class SLL:
    def __init__(self):
        self.head = None
        self.next = None
        self.tail = None
        self.lens = 0


    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count


    def insert_at_start(self, data) :
        new_node = Node()
        new_node.set_data(data)
        if self.lens == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
        self.lens += 1


    def insert_at_end(self, data):
        new_node = Node()
        new_node.set_data(data)
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)
        self.lens += 1


    def insert_at_pos(self, pos, data)    :
        if pos > self.lens or pos < 0: return None
        else:
            if pos == 0:
                self.insert_at_start(data)
            else:
                if pos == self.length:
                    self.insert_at_end(data)
                else:
                    new_node = Node()
                    new_node.set_data(data)
                    count = 0
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.get_next()
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                    self.lens += 1


    def delete_at_start(self)                :
        if self.lens == 0: return
        else:
            self.head = self.head.get_next()
            self.lens -= 1


    def delete_at_end(self):
        if self.length == 0: return
        else:
            curr_node = self.head
            prev_node = self.head
            while curr_node.get_next() != None:
                prev_node = curr_node
                curr_node = curr_node.get_next()
            prev_node.set_next(None)
            self.lens -= 1


    def delete_node(self, node):
        if self.lens == 0:
            raise ValueError('List is Empty.')
        else:
            current  = self.head
            previous = None
            found    = False
            while not found and self.lens>0:
                if current.data == node.data:
                    found = True
                    break
                else:
                    previous = current
                    if current.next:
                        current  = current.get_next()
                    else:
                        break
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

            self.lens -= 1

    def delete_value_from_list(self, value)             :
        current = self.head
        previou = self.head
        while current.next != None:
            if current.data == value:
                previou.next = current.next
                self.lens -= 1
                return
            else:
                previou = current
                current = current.next
        print("Value is not in the list.")

    def delete_at_pos(self, pos)    :
        if pos > self.lens or pos < 0:
            print("This position does not exist.")
            return
        count = 0
        current = self.head
        previou = self.head
        while current.next != None:
            count += 1
            if count == pos:
                previou.next = current.next
                self.lens -= 1
                return
            else:
                previou = current
                current = current.next

    def clear(self) :
        self.head = None

    def print_list(self):
        if self.head == None:
            print("[]")
        else:
            lst = []
            curr = self.head
            while curr.next != None:
                lst.append(curr.data)
                curr = curr.get_next()
            print(*lst)









sll = SLL()
sll.insert_at_start(12)
sll.insert_at_end(132)
sll.insert_at_pos(1, 41)
sll.insert_at_pos(2, 36)
sll.insert_at_pos(3, 14)
sll.insert_at_pos(4, 29)
sll.delete_at_end()
sll.delete_at_start()
sll.delete_at_pos(2)
sll.print_list()
node = Node()
node.set_data(14)
sll.delete_node(node)
sll.print_list()
sll.clear()
sll.print_list()



