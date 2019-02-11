'''
Given an unsorted linked list
remove all duplicate elements
b.without using buffer
'''
class linked_list_node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None
    def add_node(self, data):
        node = linked_list_node(data)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node

    def print_list(self):
        lst = []
        if self.head is not None:
            curr = self.head
            while curr.next != None:
                lst.append(curr.data)
                curr = curr.next
            lst.append(curr.data)
        print(*lst)

def remove_duplicate_from_list(ll):
    #using dictionary
    dict = {}
    previous = None
    while ll is not None:
        if ll.data in dict:
            previous.next = ll.next
        else:
            dict[ll.data] = True
            previous = ll
        ll = ll.next

def remove_duplicate_from_list_2(head)        :
    #without using any buffer
    if head is None: return
    current = head
    while current is not None:
        runner  = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next





ll = linked_list()
for i in [23, 45, 57, 12, 90, 45, 112,23, 67]:
    ll.add_node(i)
ll.print_list()
remove_duplicate_from_list_2(ll.head)
ll.print_list()



















