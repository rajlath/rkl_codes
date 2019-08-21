import sys
class Solution:
    def movesToMakeZigzag(self, nums):
        tmp = nums[:]
        def solve(nums, mode):
            ans = sys.maxsize
            now = 0
            for i in range(len(nums) - 1):
                if i %2 == mode:
                    if nums[i] >= nums[i+1]:
                        now += nums[i] - nums[i+ 1] + 1
                    nums[i] = nums[i+1]-1
                else:
                    if nums[i] <= nums[i+1]:
                        now += nums[i+1] - nums[i] + 1
                        nums[i+1] = nums[i] - 1
            ans = min(ans, now)
            return ans


        return min(solve(nums, 0), solve(tmp, 1))

print(Solution().movesToMakeZigzag([2, 1, 2]))