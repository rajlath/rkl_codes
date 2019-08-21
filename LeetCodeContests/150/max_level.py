# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = {}
        def dfs(root, level):
            if root == None:
                return
            if level not in m:
                m[level] = 0
            m[level] += root.val
            dfs(root.left, level+1)
            dfs(root.right, level + 1)
        dfs(root, 1)
        ans = 0
        now = -sys.maxsize
        #print m
        for key in m.keys():
            if m[key] > now:
                now = m[key]
                ans = key
        return ans