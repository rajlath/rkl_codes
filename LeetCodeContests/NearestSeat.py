from itertools import groupby
class Solution(object):
    def maxDistToClosest(self, seats):
        maxs = max(seats.index(1), seats[::-1].index(1))
        for seat, group in groupby(seats):
            if not seat:
                k = len(list(group))
                maxs = max(maxs,(k+1)//2)
        return maxs



sol = Solution()
print(sol.maxDistToClosest([1,0,0,0]))