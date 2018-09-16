class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None


    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def myprint(self):
        while self.top:
            print(self.top.data, end=" ")
            self.top = self.top.next
        print()

st = Stack()
st.push(12)
st.push(80)
st.push(42)
st.myprint()


def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):

            last = stack.pop()
            #print(last, ch)
            if last is '{' and ch is '}':
                continue
            elif last is '[' and ch is ']':
                continue
            elif last is '(' and ch is ')':
                continue
            else:
                return False

    if stack.size > 0:
        return False
    else:
        return True

sl = (
"{(foo)(bar)}[hello](((this)is)a)test",
"{(foo)(bar)}[hello](((this)is)atest",
"{(foo)(bar)}[hello](((this)is)a)test))"
)
for s in sl:
    m = check_brackets(s)
    print("{}: {}".format(s, m))

