import collections
class Solution(object):
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1
        return sum(count.values())  == 0

print(Solution().canReorderDoubled([3,1,3,6]))