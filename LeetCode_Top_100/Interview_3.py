class Solution:
    def pivotIndex(self, nums):
        pivot = -1
        sums  = sum(nums)
        for i in range(len(nums)):
            if (sums - nums[i]) % 2 == 0:
                pivot = i
                break
        return pivot

print(Solution().pivotIndex([-1,-1,-1,-1,-1,0]))