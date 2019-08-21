from collections import Counter
class Solution:
    def largestUniqueNumber(self, A):
        A = Counter(A)
        vals = sorted([k for k in A if A[k] == 1])
        if len(vals) > 0:
            return vals[-1]
        else:
            return - 1



print(Solution().largestUniqueNumber([9,9,8,8]))
