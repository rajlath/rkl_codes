# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

""" Creates a node with key as 'i'. If i is root,then
    it changes root. If parent of i is not created, then
    it creates parent first
"""
def createNode(parent, i, created, root):

    # If this node is already created
    if created[i] is not None:
        return

    # Create a new node and set created[i]
    created[i] = Node(i)

    # If 'i' is root, change root pointer and return
    if parent[i] == -1:
        root[0] = created[i] # root[0] denotes root of the tree
        return

    # If parent is not created, then create parent first
    if created[parent[i]] is None:
        createNode(parent, parent[i], created, root )

    # Find parent pointer
    p = created[parent[i]]

    # If this is first child of parent
    if p.left is None:
        p.left = created[i]
    # If second child
    else:
        p.right = created[i]


# Creates tree from parent[0..n-1] and returns root of the
# created tree
def createTree(parent):
    n = len(parent)

    # Create and array created[] to keep track
    # of created nodes, initialize all entries as None
    created = [None for i in range(n+1)]

    root = [None]
    for i in range(n):
        createNode(parent, i, created, root)

    return root[0]

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def remove_node(value):
    if root is None:
        return False
    if root.key = value:
        new_node = Node(0)
        new_node.left= root
        result = remove_node(new_node, value)
        


# Driver Method
parent = [-1, 0, 0, 1, 1]
root = createTree(parent)

inorder(root)