class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rite = None

root = Node("A")
n1   = Node("B")
n2   = Node("C")
n3   = Node("D")
n4   = Node("E")
root.left = n1
root.rite = n2
n1.left   = n3
n1.rite   = n4



def pre_order(roots, nodes=[]):
    nodes.append(roots.data)
    if roots and roots.left: pre_order(roots.left, nodes)
    if roots and roots.rite: pre_order(roots.rite, nodes)
    return nodes

def in_order(roots, nodes = [])    :
    if roots and roots.left: in_order(roots.left, nodes)
    nodes.append(roots.data)
    if roots and roots.rite: in_order(roots.rite, nodes)
    return nodes

def post_order(roots, nodes=[])    :
    if roots and roots.left: post_order(roots.left, nodes)
    if roots and roots.rite: post_order(roots.rite, nodes)
    nodes.append(roots.data)

    return nodes

def level_order(roots, nodes=[])    :
    queue = [roots]
    while queue:
        curr = queue.pop(0)
        nodes.append(curr.data)
        if curr and curr.left: queue.append(curr.left)
        if curr and curr.rite: queue.append(curr.rite)
    return nodes







print("Pre order is : {}".format(pre_order(root)))
print("In order is  : {}".format(in_order(root)))
print("Post order is: {}".format(post_order(root)))
print("Level order is:{}".format(level_order(root)))





