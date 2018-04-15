import sample_data

class Stack(object):

    def __init__(self, top=-1):
        self.stk = []
        self.top = top

    def is_empty(self):
        return self.top == -1

    def size(self):
        return len(self.stk)

    def push(self, data):
        self.stk.append(data)
        self.top += 1

    def pop(self):
        if not self.is_empty():
            res = self.stk[-1]
            self.stk = self.stk[:-1]
            self.top -= 1
            return res
        return None

    def peek(self):
        if not self.is_empty():
            return self.stk[self.top]

    def __str__(self):
        indx = 0
        while indx < self.size():
            print(self.stk[indx], end=" ")
            indx += 1
        return ""

import random

stack = Stack()

for i in range(10):
    #stack.push(random.randint(1, 1000))
    stack.push(sample_data.string_data(4,"ULD"))
print(stack)
stack.pop()
stack.pop()
print(stack.peek())
print(stack)





