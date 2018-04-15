class Nodes(object):
    def __init__(self,data):
        self.value = data
        self.left = None
        self.rite = None

def build_tree(ino, poo):
    pIndex = len(poo)-1
    return _build_tree(ino, poo, 0,len(ino)-1, pIndex)

def _build_tree(ino,  poo, s, e, pIndex):
    if s > e:return None
    node = Nodes(poo[pIndex])
    pIndex-=1
    if s == e: return node
    iIndex = find(ino, s, e, node.value)
    node.rite = _build_tree(ino, poo, iIndex+1, e, pIndex)
    node.left = _build_tree(ino, poo, s, iIndex-1, pIndex)
    return node
def find(arr, s, e, val):
    for i in range(s, e+1):
        if arr[i] == val:break
    return i

def pre_order(node):
    if node==None:return
    print(node.value, end=" ")
    pre_order(node.left)
    pre_order(node.rite)




ino = [x for x in input().split()]
poo = [x for x in input().split()]
root = build_tree(ino, poo)
pre_order(root)

