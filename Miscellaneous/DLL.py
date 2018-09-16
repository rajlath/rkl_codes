class Element():
    def __init__(self, value):
        self.value = value
        self.next  = None

class DLL():
    def __init__(self, head=None):
        self.head = head


    def append(self, value):
        element = Element(value)
        if self.head is None:
            self.head = element
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = element

    def pop(self):
        if self.head is None:return None
        if self.head.next is None:
            value = self.head.next.value
            self.head.next = None
            return value
        current = self.head
        while current.next.next is not None:
            current = current.next
        value = current.next.value
        current.next = None
        return value

    def peek(self):
        if self.head is None: return None
        current = self.head
        while current.next is not None:
            current = current.next
        return current.value

    def remove(self, value):
        if self.head is None:return None
        if self.head.next is None:
            self.head = None
            return True
        else:
            current = self.head
            while current.next.next is not None:
                if current.next.next.value is value:
                    self.current.next = None
                    return True
                else:
                    current  = current.next
        return None

    def insert_first(self, value):
        next_element = self.head
        self.head    = Element(value)
        self.head.next = next_element

    def delete_first(self):
        if self.head is not None:
            new_first = self.head.next
            self.head = new_first

    def search(self, srch)        :
        if self.head is None:return None
        index = -1
        current = self.head
        while current:
            index += 1
            if current.value is srch:
                break
            else:
                current = current.next
        return index

    def size(self):
        lens = 0
        if self.head is not None:
            current = self.head
            while current:
                lens += 1
                current = current.next
        return lens

    def is_empty(self):
        return self.head is None


    def __str__(self):
        result = "["
        current = self.head
        if current is not None:
            result += str(current.value)
        current = current.next
        while current:
            result += ", "+str(current.value)
            current = current.next
        result += "]"
        return result






dll = DLL()
print(dll.size())
dll.append(12)
dll.append(32)
dll.append(-24)
dll.insert_first(145)
print(dll.size())
dll.pop()
print(dll.peek())
dll.append(178)
dll.delete_first()
print(dll.search(32))
print(dll)
print(dll.size())
print(dll.is_empty())




