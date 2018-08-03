'''
Maximum Subarray

Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0 : return max(nums)
        max_till_now, curr_max = 0, 0
        for x in nums:
            curr_max = max(0, curr_max + x)
            max_till_now = max(max_till_now, curr_max)
            #print(curr_max, max_till_now)
        return max_till_now


sol = Solution()
print(sol.maxSubArray([4,-1,2,1]))