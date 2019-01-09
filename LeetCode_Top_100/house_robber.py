class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        now = 0
        last= 0
        for i in nums:
            now, last = max(last + i, now), now
        return now


print(Solution().rob([5, 11, 7, 1, 2, 8]))
