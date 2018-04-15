class Nodes(object):
    '''
    helper function for node structure
    '''
    def __init__(self,node_data):
        self.data = node_data
        self.left = None
        self.right= None

def tree_height(node):
    '''
    Compute the height of a tree--the number of nodes
    along the longest path from the root node down to
    the farthest leaf node
    '''
    if node is None:
        return 0
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

def print_node_at_level(root, level):
    '''
    print nodes at a given level and root
    '''
    if root is None: return
    if level is 1: print("{}:".format(root.data), end= " ")
    else:
        print_node_at_level(root.left, level - 1)
        print_node_at_level(root.right,level - 1)

def print_level_order(root):
    '''
    Function to  print level order traversal of tree
    '''
    h = tree_height(root)
    for i in range(1, h+1):
        print_node_at_level(root, i)

root = Nodes(1)
root.left = Nodes(2)
root.right= Nodes(12)
root.left.left = Nodes(4)
root.right.right= Nodes(5)

print_level_order(root)




