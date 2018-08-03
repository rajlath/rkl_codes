class Node(object):
    def __init__(self, data, left=None, rite=None):
        self.data = data
        self.left = left
        self.rite = rite

class BST(object):
    size = 0
    def __init__(self):
        self.root = None
        self.size = 0
    def insert_node(self, node, data):
        new_node = Node(data)
        curr = self.root
        if curr == None:
            self.root = node
        else:
            if curr.data > data:
                self.insert_node(self, curr.rite, data)
            else:
                self.insert_node(self, curr.left, data)
        return


def root_height(BST):
    return height(BST.root)

def height(node)    :
    if node == None:
        return 0
    else:
        return  1 + max(height(node.left), height(node.rite))

n = int(input())
a = [int(x) for x in input().split()]
bst = BST()
for i in range(n):
    bst.insert_node(a[i])
print(root_height(bst))
height = 0
curr = bst.root
while curr != None:
    height += height(curr)
print(height)









