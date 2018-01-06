class Deque(object):
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def is_empty(self):
        return self.items ==  []
    def add_rear(self, x):
        self.items.insert(0, x)
    def add_front(self, x):
        self.items.append(x)
    def remove_rear(self):
        rets = self.items.pop(0)
        return rets
    def remove_front(self):
        rets = self.items.pop()
        return rets


def palindrome_checker(st):
    dq = Deque()
    for i in st:
        dq.add_rear(i)
    still_equal = True
    while dq.size() > 1:
        first = dq.remove_rear()
        last  = dq.remove_front()
        if first != last:
            still_equal = False
    return still_equal

print(palindrome_checker("abcdefcba"))
print(palindrome_checker("radar"))
