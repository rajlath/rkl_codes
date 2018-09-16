
# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 13:29:38
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : Benjamin Baka PythonDSandAlgo Examples
# @Version : 1.0.0

class Nodes(object):
    '''
    Nodes implemented for use in SLL
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

class Single_link_list(object):
    '''
    Single link list implemented.
    '''
    def __init__(self):
        '''head and tail are of Nodes class'''
        self.head = None
        self.tail = None
        self.size = 0

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def append(self, data):
        node = Nodes(data)
        if self.head :
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def get_size(self):
        count = 0
        current = self.tail
        while current:
            count += 1
            current = current.next
        return count

    def delete(self, data):
        current = self.tail
        prev    = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def data_in_list(self, data):
        indx = -1
        for node in self.iter():
            indx += 1
            if data == node:
                break
        if indx == self.size-1:
            return -1
        else:
            return indx

    def print_list(self):
        lst = []
        curr = self.tail
        while curr:
            lst.append(curr.data)
            curr = curr.next
        print(*lst)

    def delete_list(self):
        self.head = None
        self.tail = None









sll = Single_link_list()
sll.append(12)
sll.append(28)
sll.append(36)
for val in sll.iter():
    print(val)
sll.delete(28)
print(sll.data_in_list(28))

sll.delete_list()
sll.print_list()












