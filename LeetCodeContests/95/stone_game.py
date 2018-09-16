class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[0] * (n+5) for _ in range(n+5)]
        for l in range(n):
            for i in range(n-l):
                dp[i][i+l] = max(piles[i] - dp[i+1][i+l], piles[i+l] - dp[i][i+l-1])
        return dp[0][n-1] > 0


print(Solution().stoneGame([5,3,4,5]))