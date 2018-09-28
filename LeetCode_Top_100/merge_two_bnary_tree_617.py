'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the
two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null node will be used as
the node of new tree.

Example 1:

Input:
    Tree 1                     Tree 2
        1                         2
        / \                       / \
        3   2                     1   3
    /                           \   \
    5                             4   7
Output:
Merged tree:
        3
        / \
    4   5
    / \   \
    5   4   7


Note: The merging process must start from the root nodes of both trees.
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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:return t2
        if t2 == None:return t1
        t1.val += t2.val
        t1.left =self. mergeTrees(t1.left, t2.left)
        t1.right= self.mergeTrees(t1.right, t2.right)
        return t1

