'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that
every key of the original BST is changed to the original key plus sum of
all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
            2   13

Output: The root of a Greater Tree like this:
             18
            /   \
           20     13
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



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Tmp = ListNode(int(-10e8))
        while head:
            Tmp.next, head.next, head = head,Tmp.next, head.next
        return Tmp.next


        #iterative
        prev = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


        #recursive
        if head is None or head.next is None:return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p