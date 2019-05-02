# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
import math
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, mins = math.inf, maxs = - math.inf):
            if node:
                mins = min(mins, node.val)
                maxs = max(maxs, node.val)
                dfs(node.left, mins, maxs)
                dfs(node.right, mins, maxs)
            else:
                self.ans = max(self.ans, maxs - mins)
        self.ans = 0
        dfs(root)
        return self.ans

print(Solution().maxAncestorDiff([8,3,10,1,6,None,14,None,None,4,7,13])) # exptecte4d answer 7

