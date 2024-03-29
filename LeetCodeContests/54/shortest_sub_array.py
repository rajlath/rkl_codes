'''
https://leetcode.com/contest/leetcode-weekly-contest-54/problems/degree-of-an-array/
697. Degree of an Array

Difficulty: Easy
Given a non-empty array of non-negative integers nums,
the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums,
that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.


'''
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        maxf = 0
        for i in range(len(nums)):
            x = nums[i]
            if x not in d:
                a = [1,i,i] #count, start, end
                d[x] = a
            else:
                a = d[x]
                a[0] += 1
                a[2] = i
            maxf = max(maxf, a[0])

        ret = len(nums)
        for x in d:
            a = d[x]
            if a[0] == maxf:
                ret = min(ret, a[2]-a[1]+1)
        return ret