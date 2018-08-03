class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xors = 0
        for i in range(len(nums)):
            xors ^= nums[i]
        return xors