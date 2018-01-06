'''
https://leetcode.com/contest/leetcode-weekly-contest-54/problems/partition-to-k-equal-sum-subsets/

698. Partition to K Equal Sum Subsets

Difficulty: Medium
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = sum(nums)
        if s%k: return False
        avg = s/k
        if max(nums) > avg: return False
        if len(nums)==1: return k==1

        left = gen(nums[:len(nums)/2], k, avg)
        right = gen(nums[len(nums)/2:], k, avg)
        for a in left:
            b = [avg-a[i] for i in range(k)]
            b.sort()
            b=tuple(b)
            if b in right:
                return True
        return False

def gen(arr, k, limit):
    cand = [tuple([0]*k)]
    for x in arr:
        tmp = set()
        for c in cand:
            for i in range(k):
                a = list(c)
                if a[i]+x > limit: continue
                a[i] += x
                a.sort()
                tmp.add(tuple(a))
        cand = tmp
    return cand
