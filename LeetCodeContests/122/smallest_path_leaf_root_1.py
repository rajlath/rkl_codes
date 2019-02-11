# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from string import ascii_lowercase as al
class Solution(object):
    ret = "~"

    def dfs(self, curr, s):
        if curr is None: return
        s = al[curr.val] + s
        if curr.left is None and curr.right is None:
            if s < self.ret:
                self.ret = s
        dfs(curr.left, s)
        dfs(curr.right, s)


    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.dfs(root, '')
        return self.ret

print(Solution().smallestFromLeaf([25,1,3,1,3,0,2]))

