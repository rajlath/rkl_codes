# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A, B):
        overlaps = []
        p = 0
        for x in A:
            for y in B:
                l = max(x[0], y[0])
                r = min(x[1], y[1])
                if l <= r:
                    overlaps.append((l, r))
        return overlaps
print(Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))
