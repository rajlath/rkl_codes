# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def bstFromPreorder(self, p):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not p:
            return None
        ret = TreeNode(p[0])
        i = 1
        while i < len(p) and p[i] < p[0]:
            i += 1
        ret.left = self.bstFromPreorder(p[1 : i])
        ret.right = self.bstFromPreorder(p[i : ])
        return ret