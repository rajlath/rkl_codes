class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rite = None




def pre_order(roots, nodes):
    nodes.append(roots.data)
    if roots and roots.left: pre_order(roots.left, nodes)
    if roots and roots.rite: pre_order(roots.rite, nodes)
    return nodes

def in_order(roots, nodes = [])    :
    if roots and roots.left: in_order(roots.left, nodes)
    nodes.append(roots.data)
    if roots and roots.rite: in_order(roots.rite, nodes)
    return nodes

# left tree
a = Node(10)
n1 = Node(4)
n2 = Node(6)
n3 = Node(30)

# setup children
a.left = n1
a.right = n2
n1.right = n3


# right tree
root_r = Node(26)
n1_r = Node(10)
n2_r = Node(3)
n3_r = Node(4)
n4_r = Node(6)
n5_r = Node(3)
n6_r = Node(30)

# setup children
n3_r.right = n6_r
n1_r.left = n3_r
n1_r.right = n4_r
n2_r.right = n5_r
root_r.left = n1_r
root_r.right = n2_r


print(pre_order(a, []))




