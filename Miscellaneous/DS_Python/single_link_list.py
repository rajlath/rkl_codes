class Nodes(object):
    def __init__(self, value,next_node=None):
        self.value = value
        self.next  = None
    def __repr__(self):
        print(self.value)


class MyLinkedList:

    def __init__(self):
        """
        Initialize linked list here.
        """
        self.head = None

    def __repr__(self):
        """
        return a string representation of the linked list
        """
        rets = []
        curr = self.head
        while curr:
            rets.append(curr.value)
            curr = curr.next
        return "[" + " ".join(map(str,rets)) + "]"


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        curr = self.head
        indx = 0
        has_index = False
        while curr:
            if indx == index:
                return curr.value
            curr = curr.next


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.head = Nodes(val, self.head)


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        prev = None
        if not self.head:
            self.head = Nodes(val)
        else:
            curr = self.head
            while curr :
                prev = curr
                curr = curr.next
            prev.next = Nodes(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list,
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

        node = Nodes(val)
        curr = self.head
        indx = 0
        prev = None
        has_index = False
        while curr:
            if indx == index:
                has_index = True
                break
            prev = curr
            curr = curr.next
            indx += 1
        if has_index:
            prev.next = node
            node.next = curr

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        indx = 0
        curr = self.head
        prev = None
        has_index = False
        while curr:
            if indx == index:
                has_index = True
                break
            prev = curr
            curr = curr.next
            indx +=1
        if has_index:
            prev.next = curr.next




mll  = MyLinkedList()
mll.addAtHead(5)
mll.addAtTail(12)
mll.addAtIndex(1, 121)
mll.deleteAtIndex(2)
print(mll)



