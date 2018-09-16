'''
889. Construct Binary Tree from Preorder and Postorder Traversal
User Accepted: 756
User Tried: 990
Total Accepted: 771
Total Submissions: 1731
Difficulty: Medium
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def make(s, t):
            if not s: return None
            node = TreeNode(s[0])
            if len(s) == 1:
                return node

            i = 0
            while t[i] != s[1]: i += 1
            node.left = make(s[1:i+2], t[:i+1])
            node.right = make(s[i+2:], t[i+1:])
            return node

        return make(pre, post)