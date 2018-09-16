class _Nodes(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL(object):
    '''
    Double Link List
    '''
    def __init__(self):
        '''
        self.head = first node
        self.tail = last  node
        self.count= size of the list
        '''
        self.head =  None
        self.tail =  None
        self.count=  0

    def iter(self)    :
        curr = self.head
        while curr:
            val = curr.data
            curr = curr.next
            yield val

    def append(self, data):
        node = _Nodes(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    def delete(self, data):
        '''
        delete a node having data = data
        '''
        curr = self.head
        if not curr: return False
        if curr.data == data:
            self.head = curr.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    node_deleted = True
                    break
                curr = curr.next
        self.count -= node_deleted

    def contains(self, data)    :
        '''
        check if data is in dll
        '''
        for it in self.iter():
            if it == data:
                return True
        return False

dll = DLL()
dll.append(102)
dll.append(82)
dll.append(18)
dll.append(12)
for it in dll.iter():
    print(it)
print(dll.count)
dll.delete(82)
print(dll.count)
for it in dll.iter():
    print(it)
print(dll.contains(1000))
print(dll.contains(12))
print(dll)




