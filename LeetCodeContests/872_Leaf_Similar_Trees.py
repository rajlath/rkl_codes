'''
Consider all the leaves of a binary tree.
From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
Both of the given trees will have between 1 and 100 nodes.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leave_1 = []
        leave_2 = []
        self.get_all_leaves(root1, leave_1)
        self.get_all_leaves(root2, leave_2)
        return leave_1 == leave_2
    def get_all_leaves(self, root, leaves):
        if root.left != None and root.right == None:
            leaves.append(root.val)
        else:
            for x in (root.left, root.right)    :
                if x is not None:
                    return self.get_all_leaves(x, leaves)


#solution 2
#
#
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def fringe(root):
            result = []
            if root.left:
                result.extend(fringe(root.left))
            if root.right:
                result.extend(fringe(root.right))
            if not result:
                result = [root.val]
            return result
        return fringe(root1) == fringe(root2)



