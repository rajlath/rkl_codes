class Nodes(object):
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

class Binary_tree(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        nodes = Node(self, value)
        if self.head == None:
            self.head = nodes

    def add_to(self, nodes, value):
        




