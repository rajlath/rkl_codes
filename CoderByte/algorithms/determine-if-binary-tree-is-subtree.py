class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

root  = Node(10)
n1    = Node(4)
n2    = Node(6)
n3    = Node(30)

n1.right = n3
root.left= n1
root.right=n2

root_r =  Node(26)
n1_r =  Node(10)
n2_r =  Node(3)
n3_r =  Node(4)
n4_r =  Node(6)
n5_r =  Node(3)
n6_r =  Node(30)

# setup children
n3_r.right = n6_r
n1_r.left  = n3_r
n1_r.right = n4_r
n2_r.right = n5_r
root_r.left = n1_r
root_r.right = n2_r




def pre_order(root, node=[]):
    if root:node.append(root.data)
    if root and root.left:(pre_order(root.left, node))
    if root and root.right:(pre_order(root.right, node))
    return node

def in_order(root, node=[]):
    if root and root.left:(in_order(root.left, node))
    if root:node.append(root.data)
    if root and root.right:(in_order(root.right, node))
    return node



def is_subtree(A, B):
    rpre = "_".join(map(str,pre_order(A)))
    rin  = "_".join(map(str,in_order(A)))
    r_rpre = "_".join(map(str,pre_order(B)))
    r_rin  = "_".join(map(str,in_order(B)))
    return rpre in r_rpre or rin in r_rin

print(is_subtree(root, root_r))



