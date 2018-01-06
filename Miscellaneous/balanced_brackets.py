class Stack():
    def __init__(self):
        self.items = []
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


def par_checker(symstr):
    stk = Stack()
    is_balanced = True
    for i in symstr:
        if i == "(":
            stk.push(i)
        else:
            if stk.is_empty():
                is_balanced = False
            else:
                stk.pop()
    return is_balanced and stk.is_empty()


def all_par_checker(symstr):
    stk = Stack()
    left = "({["
    rite = ")}]"
    is_balanced = True
    for i in symstr:
        if i in left:
            stk.push(i)
        else:
            if stk.is_empty():
                is_balanced = False
            else:
                last = stk.pop()

                if left.index(last) != rite.index(i):
                    is_balanced = False

    return is_balanced and stk.is_empty()



print(par_checker('((()))'))
print(par_checker('(()'))


print(all_par_checker('{{([][])}()}'))
print(all_par_checker('[{()]'))










