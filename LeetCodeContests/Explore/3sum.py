'''
3Sum
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array
which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if nums == None or len(nums) < 3:return result
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i-1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:j += 1
                        while j < k and nums[k] == nums[k+1]:k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0: j += 1
                    else:k -= 1

        return result

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))




