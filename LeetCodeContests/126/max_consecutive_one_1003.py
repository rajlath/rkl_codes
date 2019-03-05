class Solution:
    def longestOnes(self, A, k):
        cnts, s, q = 0. -1, []
        for i, v in enumerate(A):
            if v == 0:
                q.append(i)
                if len(q) > k:
                    s = q.pop(0)
            sol = max(sol, i - s)
        return sol
