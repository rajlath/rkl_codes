import queue
class Nodes(object):

    """A class for nodes to be used in graph, BST etc"""
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right= None

def insert_bst(root, node):
    if root == None:
        root = node
    else:
        if root.data >  node.data:
            if root.left is None:
                root.left = node
            else:
                insert_bst(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_bst(root.right, node)



def pre_order_traverse(root):
    if root == None:return
    print(root.data)
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)

def in_order_traverse(root):
    if root == None:return
    in_order_traverse(root.left)
    print(root.data, sep=" ")
    in_order_traverse(root.right)

def BST_height(root):
    if root == None:return -1
    left_height = BST_height(root.left) + 1
    right_height= BST_height(root.right) + 1
    return max(left_height, right_height)

def validate_BST(root):
    elems = []
    if root == None:return
    in_order_traverse(root.left)
    elems.append(root.data)
    in_order_traverse(root.right)
    valid = True
    for i in range(1,len(elems)):
        if elems[i] <= elems[i-1]:
            valid = False
            break
    return valid
def LCA_in_BST(root, v1, v2):
    if root.data > v1 and root.data > v2:LCA_in_BST(root.left, v1, v2)
    if root.data < v1 and root.data < v2:LCA_in_BST(root.right, v1, v2)
    return root


    '''
    delete a value N from a BST
    if left child of N is None:replace N with right child
    if right child of N is None: replace N with left child
    if none of the child is None:
        a. replace N with minimum value node in right subtree
        b. replace N with minimum value node in left  subtree
    '''
def delete_a_Node_solution1(root, N):
        '''
        option areplace N with minimum value node in right subtree
        '''
        if root == None:return None
        if root.data > N :
            root.left = solution1(root.left, N)
        elif root.data < N:
            root.right = solution1(root.right, N)
        else:
            if root.left == None:return root.right
            elif root.right == None:return root.left
            else:
                tmp = root.right
                while tmp.left != None:
                    tmp = tmp.left
                newroot = tmp.data
                root.data = newroot
                root.right = solution1(root.right, temp.data)
        return root

def delete_a_Node_solution2(root, N):
    '''
    option b replace N with minimum value node in left subtree
    '''
    if root == None:return None
    if root.data > N :
        root.left = delete_a_Node_solution2(root.left, N)
    elif root.data < N:
       root.right = delete_a_Node_solution2(root.right, N)
    else:
        if root.left == None:return root.right
        elif root.right == None:return root.left
        else:
            tmp = root.left
            while tmp.right != None:
                tmp = tmp.right
            newroot = tmp.data
            root.data = newroot
            root.left = delete_a_Node_solution2(root.left, tmp.data)
    return root


def max_in_path(root, x):
    '''
    this function find max in path from root node to node x
    '''
    if root.data == x : return x
    if root.data > x:return max(max_in_path(root.left, x), root.data)
    if root.data < x:return max(max_in_path(root.right, x), root.data)

def max_in_path_from_a_to_b(root, a, b):
    '''
    Finding maximum (or minimum) in path from node A to node B
    '''
    lca = LCA_in_BST(root, a, b)
    ans = max(max_in_path(lca, a), max_in_path(lca, b))
    return ans

def min_in_path(root, x):
    '''
    this function find max in path from root node to node x
    '''
    if root.data == x : return x
    if root.data > x:return min(min_in_path(root.left, x), root.data)
    if root.data < x:return min(min_in_path(root.right, x), root.data)

def min_in_path_from_a_to_b(root, a, b):
    '''
    Finding maximum (or minimum) in path from node A to node B
    '''
    lca = LCA_in_BST(root, a, b)
    ans = min(min_in_path(lca, a), min_in_path(lca, b))
    return ans




arr = [500, 400, 300, 450, 425, 475, 600, 550]
r = Nodes(arr[0])
for i in arr[1:]:
   insert_bst(r, Nodes(i))
print(BST_height(r))

totalHeightSum = 0
def calculateHeightAndAdd (n):
    global totalHeightSum
    if n is None:return 0
    leftHeight = calculateHeightAndAdd(n.left)
    rightHeight= calculateHeightAndAdd(n.right)
    myHeight = 1 + max ( leftHeight, rightHeight )
    totalHeightSum += myHeight
    return totalHeightSum



print(calculateHeightAndAdd(r))




