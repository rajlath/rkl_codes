'''
Sort Colors
  Go to Discuss
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total
number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''
from collections import Counter
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        This solution uses count sort using two pass algorithm.
        """
        numsc = Counter(nums)
        reds, white, blue = numsc[0], numsc[1], numsc[2]
        for i in range(len(nums)):
            if reds > 0:
                nums[i] = 0
                reds -= 1
                continue
            elif white > 0:
                nums[i] = 1
                white -= 1
                continue
            else:
                nums[i] = 2


        return nums


class Solution1:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        This solution one pass algorithm.
        """
        reds = 0
        blue = len(nums)-1
        i = 0
        while i < (blue + 1):
            #print(nums[i])
            if nums[i] == 0:
                nums[i], nums[reds] = nums[reds], nums[i]
                reds += 1
                i += 1
                continue
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
                continue
            i += 1


        return nums

print(Solution1().sortColors([1,2,0]))
