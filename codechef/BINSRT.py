class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)

series = [3, 5, 8]
for i in range(0, len(series), 3)
    root, left, rite = series[i:i+3]
    print(root, left, rite)


