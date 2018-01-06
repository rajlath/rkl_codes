'''
742. Closest Leaf in a Binary Tree My SubmissionsBack to Contest
Difficulty: Medium
Given a binary tree where every node has a unique value, and a target key k,
find the closest leaf node to target k in the tree.

A node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row.
The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the closest leaf node to 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The closest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is closest to the node with value 2.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.isLeaf = set()
        self.repo = {}
        self.buildEdges(root)

        visited = set()
        queue = collections.deque([k])

        while queue:
            node = queue.popleft()
            if node in self.isLeaf:
                return node
            else:
                visited.add(node)
                for n in self.repo[node]:
                    if n not in visited:
                        queue.append(n)
            #print queue

    def buildEdges(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.isLeaf.add(node.val)

        if node.left is not None:
            self.repo.setdefault(node.val, []).append(node.left.val)
            self.repo.setdefault(node.left.val, []).append(node.val)
            self.buildEdges(node.left)

        if node.right is not None:
            self.repo.setdefault(node.val, []).append(node.right.val)
            self.repo.setdefault(node.right.val, []).append(node.val)
            self.buildEdges(node.right)

