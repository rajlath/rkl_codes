class Stack(object):
    def __init__(self):
        self.lst = []

    def push(self, vals):
        self.lst.append(vals)
    def pops(self):
        if len(self.lst) > 0:
            return self.lst.pop()
    def peeks(self):
        if len(self.lst) > 0:
            curr = self.lst[-1]
            return curr

stack = Stack()
nops = int(input())
for _ in range(nops):
    curr = [x for x in input().split()]
    ops  = curr[0]
    if ops == 'PUSH':
        stack.push(int(curr[1]))
    elif ops == "PEEK":
        print(stack.peeks())
    elif ops == "POP":
        stack.pops()
print(sum(stack.lst))


