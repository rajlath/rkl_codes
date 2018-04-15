class Nodes(object):
    '''
    building blocks of a single link list
    '''
    def __init__(self, val):
        '''
        initialize a node.
        param data : a value for the node
        '''
        self.data = val
        self.next = None

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, val):
        self.data = val
    def set_next(self, val):
        self.next = val

class Linked_List(object):
    '''
    defines a list of nodes instances
    '''
    def __init__(self):
        self.head = None
    def is_empty(self):
        '''
        check if list is empty
        '''
        return self.head == None
    def size(self):
        '''
        find the size of list i.e node counts
        '''
        cnt = 0
        curr = self.head
        while curr is not None:
            cnt += 1
            curr = curr.next
        return cnt

    def add(self, item):
        '''
        add a node at start replacing current head with this node
        '''
        new_node = Nodes(item)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, val):
        '''
        search for a node value val in the linked_list
        return True if found else return False
        '''
        found = False
        curr = self.head
        while curr is not None and not found:
            if curr.get_data() is val:
                found = True
            else:
                curr = curr.get_next()
        return found

    def remove(self,vals):
        '''
        remove vals from list if found else raise error
        '''
        found = False
        curr  = self.head
        previous = None
        while curr is not None and not found:
            if curr.get_data() is vals:
                found = True
            else:
                previous = curr
                curr     = curr.get_next()
        if found:
            if previous is not None:
                self.head = self.head.get_next()
            else:
                previous.set_next(curr.get_next())
        else:
            raise ValueError
            print("Not found")
            return False

    def insert(self, vals, position):
        '''
        insert a node at position
        if position is not availble, raise indexError
        '''
        if position > self.size() - 1:
            raise IndexError
            print("Out of bound position")
        pos = 0
        curr  = self.head
        previous = None
        if position == 0:
            self.add(vals)
        else:
            new_node = Nodes(vals)
            while pos < position:
                pos += 1
                previous = curr
                curr = curr.get_next()
            previous.set_next(new_node)
            new_node.set_next(curr)



    def index(self, vals):
        '''
        return index where this value is found.
        else return None
        '''
        pos = 0
        found = False
        curr  = self.head
        previous = None
        while curr is not None and not found:
            if curr.get_data() is vals:
                return pos
            else:
                previous = curr
                curr = curr.get_next()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position=None):
        '''
        return and remove node at position
        if position is out of bound raise index error
        if position is not provided return and remove head node data
        '''
        if position is not None and position > self.size():
            print("position is not available")
            raise IndexError
        curr = self.head
        previous = None
        pos = 0

        if position == None:
            rets = self.head.get_data()
            self.head = self.head.get_next()
        else:
            while pos < position:
                previous = curr
                curr = curr.get_next()
                pos += 1
                rets = curr.get_data()
            previous.set_next(curr.get_next())
        return rets
        print(rets)

    def append(self, vals):
        '''
        appends a node at the last
        '''
        current = self.head
        previous= None
        pos     = 0
        lens    = self.size()
        while pos < lens:
            previous = current
            current = current.get_next()
            pos += 1
        new_node = Node(vals)
        if previous is None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            current.set_next(new_node)

    def print_list(self):
        '''
        prints list
        '''
        current = self.head
        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_next()

sll = Linked_List()
sll.add(12)
sll.add(45)
sll.insert(36, 0)
sll.insert(81, 2)
print(sll.search(45))
print(sll.index(45))
sll.print_list()
sll.pop()
sll.pop(1)
sll.print_list()




























