'''
print nth to last node value in linked list
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

def nth_to_last(head, n):
    if head is None:return 0
    i = nth_to_last(head.next, n) + 1
    if i == n:
        print(head.data)
    return i

ll = linked_list()
for i in [23, 45, 57, 12, 90, 45, 112,23, 67]:
    ll.add_node(i)
ll.print_list()
n = 9
i = nth_to_last(ll.head, n)
if i < n:
    print("{}th element is out of list having {} nodes.".format(n, i))
ll.print_list()



















