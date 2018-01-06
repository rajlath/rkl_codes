class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, x):
        self.items.insert(0, x)

    def dequeue(self):
        rets = self.items.pop()
        return rets

    def size(self):
        return len(self.items)

    def __str__(self):
        st = "["
        for i in self.items:
            if i != self.items[-1]:
                st +=  str(i) + ","
            else:
                st +=  str(i)+"]"
        return st

def hot_potato(lst, num):
    q = Queue()
    for i in lst:
        q.enqueue(i)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return (q.dequeue())

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],2))


