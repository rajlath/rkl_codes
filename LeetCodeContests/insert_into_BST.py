# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        node = TreeNode(val)
        if root is None:
            return node
        curr = root
        while True:
            if curr.val > val:
                if curr.left is None:
                    curr.left = node
                    break
                curr = curr.left
            else:
                if curr.right < val:
                    if curr.right is None:
                        curr.right = node
                        break
                    curr = curr.right
        return root
