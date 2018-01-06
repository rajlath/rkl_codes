'''
719. Find K-th Smallest Pair Distance My SubmissionsBack to Contest

Difficulty: Hard
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B)
is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''
def numOfPairs(nums, d):
    res  = 0
    l, r = 0, 0
    while l < len(nums) - 1:
        while r < len(nums) - 1 and nums[r + 1] <= nums[l] + d:
            r += 1
            res += 1
        l += 1
        if r >= l:
            res += r - l
        else:
            r = l
    return res


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        high = nums[-1] - nums[0]
        low = high
        for i in range(1, len(nums)):
            low = min(low, nums[i] - nums[i-1])
        while high > low:
            middle = (high + low) // 2
            if numOfPairs(nums, middle) < k:
                low = middle + 1
            else:
                high = middle
        return high

sols = Solution()
print(sols.smallestDistancePair([1,3,1], 1))