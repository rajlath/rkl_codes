'''
153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you
beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''
# -*- coding: utf-8 -*-
# @Date    : 2018-09-08 19:09:43
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]

class Solution(object):
    def findMin(self, nums):
        """
         :type nums: List[int]
         :rtype: int
        """
        if len(nums)==1:return nums[0]
        left = 0
        rite = len(nums) - 1
        if nums[rite] > nums[0]:
            return nums[0]
        while rite > left:
            mid = (left + rite) // 2
            if nums[mid] > nums[mid + 1]: return nums[mid + 1]
            if nums[mid - 1] > nums[mid]: return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                rite = mid - 1

from collections import deque

dq = deque(range(512,2000))
dq.rotate(456)
nums = list(dq)
print(Solution().findMin(nums))



