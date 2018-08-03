# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[TreeNode]
        """
        edges = collections.defaultdict(list)
        nodes = {}

        def make_graph(node):
            if node.left:
                edges[node].append(node.left)
                edges[node.left].append(node)
                make_graph(node.left)
            if node.right:
                edges[node].append(node.right)
                edges[node.right].append(node)
                make_graph(node.right)

        make_graph(root)
        ans = []
        q = [target]
        seen = set(q)

        for _ in range(K):
            if not q: break
            q2 = []
            for i in q:
                for j in edges[i]:
                    if j not in seen:
                        seen.add(j)
                        q2.append(j)
            q = q2
        return [x.val for x in q]

sol = Solution()
print(sol.distanceK([3,5,1,6,2,0,8,None,None,7,4],5, 2))