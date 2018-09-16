class _Nodes(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return  str(self.data)

class SLL(object)        :
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data)    :
        node = _Nodes(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
           self.tail = node
           self.head = node
        self.size += 1


    def iter(self)    :
        curr = self.tail
        while curr:
            val = curr.data
            curr= curr.next
            yield val

    def delete(self, data)        :
        '''
        delete a node having this data
        '''
        curr = self.tail
        prev = self.tail
        while curr:
            if curr.data == data:
                if self.tail == curr:
                    self.tail= curr.next
                else:
                    prev.next = curr.next
                self.size -= 1
                #print(self.size)
                return
            prev = curr
            curr = curr.next


    def is_data_in_sll(self, data):
        curr = self.tail
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def clear(self)    :
        self.tail = None
        self.head = None










sll = SLL()
sll.append(7)
sll.append(8)
sll.append(112)
sll.append(52)
print(sll.is_data_in_sll(112))
sll.delete(112)
print(sll.is_data_in_sll(112))
for it in sll.iter():
    print(it)
sll.clear()
print(sll.is_data_in_sll(7))














