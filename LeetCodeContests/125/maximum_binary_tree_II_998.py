# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root, val):
        if not root or val > root.val:
            r = TreeNode(val)
            r.left = root
            return r
        p, c = root, root.right
        while c and c.val > val: p, c = c, c.right
        p.right = TreeNode(val)
        p.right.left = c
        return root