# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.root = root
        if root is None: return False
        self.has_to_be = root.val

        def check(self, root, vals):
            if root.val != vals:return False
            if root and root.left: check(root.left, vals)
            if root and root.right:check(root.right, vals)
            return True
        return check(self.root, self.has_to_be)

