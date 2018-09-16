# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if self.t1 != None and self.t2 != None:
            merged_tree = TreeNode(t1.val + t2.val)
            merged_tree.left = self.mergeTrees(t1.left, t2.left)
            merged_tree.right= self.mergeTrees(t1.right + t2.right)
        elif self.t2 == None:
            merged_tree = TreeNode(t1.val)
            merged_tree.left = self.mergeTrees(t1.left,None)
            merged_tree.right= self.mergeTrees(t1.right,None)
        elif self.t1 == None:
            merged_tree = TreeNode(t2.val)
            merged_tree.left = self.mergeTrees(None, t2.left)
            merged_tree.right= self.mergeTrees(None, t2.right)
        else:
            merged_tree = None
        return merged_tree    
