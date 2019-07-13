class AppendCmd():
    def execute(self, stack, value):
        self.length = len(value)
        stack.extend(value)

    def revert(self, stack):
        for _ in xrange(self.length):
            stack.pop()

class EraseCmd():
    def execute(self, stack, value):
        self.text = stack[-value:]
        for _ in xrange(value):
            stack.pop()
         
    def revert(self, stack):
        stack.extend(self.text)

class CustomStack:
    def __init__(self):
        self.stack = []
        self.cmds = []

    def push(self, value):
        cmd = AppendCmd()
        cmd.execute(self.stack, value)
        self.cmds.append(cmd)

    def pop(self, value):
        cmd = EraseCmd()
        cmd.execute(self.stack, value)
        self.cmds.append(cmd)

    def get(self, value):
        print self.stack[value]

    def revert(self):
        cmd = self.cmds.pop()
        cmd.revert(self.stack)

def main():

    cs = CustomStack()

    N = int(raw_input())

    for _ in xrange(N):
        unknown = raw_input()

        command = unknown[0]

        if command == '1':
            cmd, value = unknown.split()
            cs.push(list(value))
        elif command == '2':
            cmd, value = map(int, unknown.split())
            cs.pop(value)
        elif command == '3':
            cmd, value = map(int, unknown.split())
            cs.get(value - 1)
        else:
            cs.revert()


if __name__ == '__main__':
    main()
