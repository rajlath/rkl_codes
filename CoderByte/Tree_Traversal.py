class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.rite = None

root = Node("A")
Nod1 = Node("B")
Nod2 = Node("C")
Nod3 = Node("D")
Nod4 = Node("E")

root.left = Nod1
root.rite = Nod2
Nod1.left = Nod3
Nod1.rite = Nod4

def pre_order(root, rets):
    rets.append(root.data)
    if root and root.left:
        pre_order(root.left, rets)
    if root and root.rite:
        pre_order(root.rite, rets)
    return rets

#print(pre_order(root, []))

def in_order(root, rets):
    if root and root.left:
        in_order(root.left, rets)
    rets.append(root.data)
    if root and root.rite:
        in_order(root.rite, rets)
    return rets

#print(in_order(root, []))

def post_order(root, rets):
    if root and root.left :
        post_order(root.left, rets)
    if root and root.rite :
        post_order(root.rite, rets)
    rets.append(root.data)
    return rets

#print(post_order(root, []))

def level_order(root, rets):
    queue = [root]
    while queue:
        curr = queue.pop(0)
        rets.append(curr.data)
        if curr.left:
            queue.append(curr.left)
        if curr.rite:
            queue.append(curr.rite)
        
    return rets

print(level_order(root, []))

