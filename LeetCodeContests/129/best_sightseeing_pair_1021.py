class Solution:
    def maxScoreSightseeingPair(self, A):
        maxs = int(-10e20)
        maxh = maxs // 2
        for i, v  in enumerate(A):
            maxs = max(maxs, maxh + v - i)
            maxh = max(maxh, v + i)
        return maxs

print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))

