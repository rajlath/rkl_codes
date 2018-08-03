class Stack():
    def __init__(self):
        self.stk = []
    def push(self, item)    :
        self.stk.append(item)
    def size(self)    :
        return len(self.stk)
    def pop(self)    :
        if self.size():
            return self.stk.pop()



def evaluate(strs):
    ops  = Stack()
    vals = Stack()

    token= [x for x in strs.split(" ")]
    i = 0
    while i < len(token):
        s = token[i]
        i += 1
        if s == "(":
            pass
        elif s in "+-*/":
            ops.push(s)
        elif s == ")":
            ops1 = ops.pop()
            v   = vals.pop()
            if ops1 == "+": v += vals.pop()
            if ops1 == "-": v -= vals.pop()
            if ops1 == "*": v *= vals.pop()
            if ops1 == "/": v /= vals.pop()
            vals.push(v)
        else:
            vals.push(float(s))

    return vals.pop()


print(evaluate("( ( 1 + 2.0  ) / 2.0 )"))



