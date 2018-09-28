'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and
others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not
count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
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



class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #return list(set(range(1, len(nums) + 1)) - set(nums))
        dict = {i:False for i in range(1, len(nums)+1)}
        for i in nums:
            dict[i] = True
        return [x for x in range(1, len(nums)+1) if not dict[x]]

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {i:False for i in range(1, len(nums)+1)}
        for i in nums:
            dict[i] = True
        return [x for x in range(1, len(nums)+1) if not dict[x]]

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))


