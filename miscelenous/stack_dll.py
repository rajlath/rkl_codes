class stack_nodes(object):
    def __init__(self, items, n_link=None):
        self.items = items
        self.next = n_link

class stack(object):
    def __init__(self):
        self.top = None
        self.size= 0

    def is_empty(self):
        return self.top==None

    def size(self):
        return self.size

    def peek(self):
        assert not self.is_empty(), "Cannot peek empty stack"
        return self.top.items

    def pop(self):
        assert not self.is_empty(), "cannot pop from an empty stack"
        curr = self.top
        self.top = self.top.next
        self.size -= 1
        return curr.items

    def push(self, items):
        curr = self.top
        self.top = stack_nodes(items)
        self.top.next = curr
        self.size+=1

    def __str__(self):
        if self.is_empty():
            return "stack is empty"
        else:
            lst = "["
            l = self.size
            curr = self.top
            while l > 0:
                lst += str(curr.items)+" "
                curr = curr.next
                l-=1
            lst += "]"
            return lst





stk = stack()
print(stk.size)  ##0
print(stk.is_empty()) # True
stk.push(12)
stk.push(84)
stk.push(36)
stk.push(21)
print(stk.size)
#print(stk)
print(stk.pop())
stk.push(41)
print(stk.size)
#print(stk)
print(stk.peek())
print(stk)






