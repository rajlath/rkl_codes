'''
866. Smallest Subtree with all the Deepest Nodes

Difficulty: Medium
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
A node is deepest if it has the largest depth possible among any node in the entire tree.
The subtree of a node is that node, plus the set of all descendants of that node.
Return the node with the largest depth such that it contains all the deepest nodes in it's subtree.

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:
We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.


Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mxdep(self, root):
        if root is None:
            return -1
        v = 1 + max([self.mxdep(node) for node in (root.left, root.right)])
        root.mxd = v
        return v

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        mx = self.mxdep(root)
        cur = root
        while True:
            if cur.left is None:
                if cur.right is None:
                    return cur
                cur = cur.right
            elif cur.right is None:
                cur = cur.left
            else:
                if cur.left.mxd > cur.right.mxd:
                    cur = cur.left
                elif cur.left.mxd < cur.right.mxd:
                    cur = cur.right
                else:
                    return cur

from collections import Counter

class Solution:
    def __init__(self):
        self.cnt = Counter()
        self.target_d = -1
        self.target_nr = -1
        self.solution = None

    def rec1(self, node, cur_d):
        if not node:
            return

        self.cnt[cur_d] += 1
        self.rec1(node.left, cur_d + 1)
        self.rec1(node.right, cur_d + 1)

    def rec2(self, node, cur_d):
        if not node:
            return 0

        result = 0

        if cur_d == self.target_d:
            result += 1

        result += self.rec2(node.left, cur_d + 1)
        result += self.rec2(node.right, cur_d + 1)

        if result == self.target_nr:
            if not self.solution:
                self.solution = node

        return result

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.cnt = Counter()
        self.rec1(root, 0)

        self.target_d = max(self.cnt.keys())
        self.target_nr = self.cnt[self.target_d]

        self.solution = None

        self.rec2(root, 0)

        return self.solution
