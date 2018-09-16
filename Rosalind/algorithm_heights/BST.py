class Node(object):
    def __init__(self, data, left=None, rite=None):
        self.data = data
        self.left = left
        self.rite = rite

class Tree(object):
    '''
    implementation of BST and related routines
    '''
    def __init__(self, data, left=None, rite=None):
        self.data = data
        self.left = left
        self.rite = rite

def parent_node(root, node_data)        :
    '''
    find parent of a node in a BST identified by root :
    '''
    parent = -1
    while root is not  None:
        if root.data is node_data:
            break
        elif node_data < root.data:
            parent = root.data
            root   = root.left
        else:
            parent = root.data
            root   = root.rite
    if root is None:
        return -1
    else:
        return parent

def level_of_node(root, node_data) :
    level = 0
    while root is not None:
        if node_data is root.data:
            break
        elif node_data < root.data:
            root = root.left
        else:
            root = root.rite
        level += 1
    return level

def sum_of_cousin(root, p, level1, level):
    sums = 0
    if root is None:   return 0
    if p == root.data: return 0
    if level == level1:return root.data
    else:
        sums += ( sum_of_cousin(root.left,p, level1+1, level) + sum_of_cousin(root.rite,p, level1+1, level))
    return sums

def print_given_level(root, node, level):
    if root is None and level < 2:return
    if level is 2:
        if root.left is node or root.rite is node:return
        if root.left:print("{}".format(root.left.data))
        if root.rite:print("{}".format(root.rite.rite))
    elif level > 2:
        print_given_level(root.left, node, level - 1)
        print_given_level(root.rite, node, level - 1)


def print_cousins(root, node)     :
        level = level_of_node(root, node)
        print_given_level(root, node, level)



root = Node(15)
root.left = Node(13)
root.left.left = Node(12)
root.left.right= Node(14)
root.rite = Node(20)
root.rite.left = Node(18)
root.rite.rite = Node(22)

Node_data = 12
p = parent_node(root, Node_data)
if p == -1:print(-1)
else:
    level = level_of_node(root, Node_data)
    sums  = sum_of_cousin(root, p, 0, level)
print(sums)
print_given_level(root,18, 3 )
level = level_of_node(root, 18)
print(print_cousins(root, 14))




