from collections import Counter
class Solution:
    def longestArithSeqLength(self, A):
        n = len(A)
        dp=[Counter() for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                ans = max(ans, dp[i][diff])
        return ans + 1


print(Solution().longestArithSeqLength([9,4,7,2,10])) # exptected 3