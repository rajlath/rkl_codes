class Stack():
    def __init__(self, items=[]):
        self.items = items
    def is_empty(self):
        return self.items == []
    def push(self, obj):
        self.items.append(obj)
    def pop(self):
        rets = self.items[-1]
        self.items = self.items[:-1]
        return rets
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        rets = "["
        for i,v in enumerate(self.items):
            if i == self.size()-1:
                rets += str(v) +"]"
            else:
                rets += str(v) +","
        return rets








