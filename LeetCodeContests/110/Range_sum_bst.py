# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        ans = 0
        if root.val in range(L, R+1):
            ans += root.val
        if root.left != None:
            ans += rangeSumBST(root.left)
        if root.right != None:
            ans += rangeSumBST(root.right)
        return ans



print(Solution().rangeSumBST([10,5,15,3,7,None,18], 7, 15))