# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from string import ascii_lowercase as al
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        path = []
        r = [None]
        def dfs(node):
            if not node: return
            path.append(al[node.val])
            try:
                if not node.left and not node.right:
                    s = ''.join(reversed(path))
                    if r[0] is None or s < r[0]: r[0] = s
                    return
                dfs(node.left)
                dfs(node.right)
            finally: path.pop()
        dfs(root)
        return r[0]