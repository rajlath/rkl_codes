class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

#setup tree

root = Node("A")
n1   = Node("B")
n2   = Node("C")
n3   = Node("D")
n4   = Node("E")

#setup tree
root.left = n1
root.right= n2
n1.left = n3
n1.right= n4

def pre_order(root, nodes=[]):
    ''' root.data root.left root.right'''
    nodes.append(root.data)
    if root and root.left:pre_order(root.left, nodes)
    if root and root.right:pre_order(root.right, nodes)
    return nodes
seq = pre_order(root)
print("Pre order sequence is " ,end=' ')
print(*seq)

def in_order(root, nodes = []):
    ''' root.left root.data root.right'''
    if root and root.left: in_order(root.left, nodes)
    nodes.append(root.data)
    if root and root.right:in_order(root.right, nodes)
    return nodes

seq = in_order(root)
print("In order sequence is ", end=' ')
print(*seq)

def post_order(root, nodes=[]):
    ''' root.left root.right root.data'''
    if root and root.left:post_order(root.left, nodes)
    if root and root.right:post_order(root.right, nodes)
    nodes.append(root.data)
    return nodes

seq = post_order(root,[])
print("Post order sequence is ", end=" ")
print(*seq)

def level_order(root, nodes=[]):
    '''add root to queue,
       while queue pop queue
       add children of poped nodes to queue()'''
    queue = [root]
    while queue:
        node = queue.pop()
        nodes.append(node.data)
        if node.left != None: queue.insert(0, node.left)
        print
        if node.right!= None: queue.insert(0, node.right)
    return nodes

seq = level_order(root, [])
print("level order seq is :", end=' ')
print(*seq)