class Nodes(object):
    '''
    Nodes class required for unordered list
    '''
    def __init__(self, initdata):
        '''
        create a new node
        '''
        self.data = initdata
        self.next = None
    def get_data(self):
        return self.data
    def set_data(self, x):
        self.data = x
    def get_next(self):
        return self.next
    def set_next(self, nnext):
        self.next = nnext

class UnOrderedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, x):
        tmp = Nodes(x)
        tmp.set_next(self.head)
        self.head = tmp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, x):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == x:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, x):
        current = self.head
        previous= None
        found   = False
        while not found:
            if current.get_data() == x:
                found = True
            else:
                previous = current
                current  = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __str__(self):
         current = self.head
         st = "Head :"
         while current != None:
             n = current.get_data()
             st +=  str(n) +"->"
             current = current.get_next()
         st +=  "None"
         return st

    def append(self, x):
        current = self.head
        while current.next != None:
            current = current.next
        tmp = Nodes(x)
        current.next = tmp

    def get_index(self, x):
        current = self.head
        index = -1

        while current.next != None:
            index += 1
            if current.get_data() == x:
                break
            current = current.get_next()
        return index

    def get_item(self, indx):
        current = self.head
        if self.size()-1 < indx:
            return None
        for i in range(indx):
            current = current.get_next()
        return current.data

    def pop(self, pos):
        rets = self.get_item(pos)
        self.remove(rets)
        return rets

    def insert(self, x, indx):
        if indx + 1 > self.size() or indx < 0:
            return "Invalid index"
        current = self.head
        for i in range(indx-1):
            current = current.get_next()
        tmp = Nodes(x)
        tmp.set_next(current.get_next())
        current.set_next(tmp)







ol = UnOrderedList()
print(ol.is_empty())
ol.add(5)
print(ol)
ol.add(8)
ol.add(42)
ol.add(32)
ol.add(11)
ol.add(81)
print(ol.size())
print(ol)
ol.remove(42)
print(ol)
print(ol.search(5))
print(ol.size())
ol.append(101)
print(ol)
print(ol.size())
print(ol.get_index(11))
print(ol.get_item(3))
print(ol.pop(3))
print(ol)
ol.insert(132, 4)
print(ol)







