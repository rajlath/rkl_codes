class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xors = 0
        for i in nums:
            xors ^= i
        return xors    