'''
Invert a binary tree.
Example:
Input:
    4
/   \
2     7
/ \   / \
1   3 6   9
Output:
    4
/   \
7     2
/ \   / \
9   6 3   1
'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-25 09:09:17
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root : return None
        right = invertTree(root.right)
        left  = invertTree(root.left)
        root.left = right
        root.right= left
        return root