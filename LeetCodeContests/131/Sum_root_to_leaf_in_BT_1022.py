# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sumRootToLeaf(self, root):
        self.ans = 0
        def DFS(node, sums):
            if node is not None:
                sums = sums * 2 + node.val
                if node.left is  None and node.right is None:
                    self.ans += sums
                DFS(node.left, sums)
                DFS(node.right, sums)
        DFS(root, 0)
        return self.ans

print(Solution().sumRootToLeaf([1,0,1,0,1,0,1]))




