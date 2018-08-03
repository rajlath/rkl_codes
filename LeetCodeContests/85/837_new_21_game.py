class Solution(object):
    def new21Game(self, N, K, W):

        dp = [0.0] * (K + W + 1)
        for i in range(N + 1, K + W):
            dp[i] = 0.0
        for i in range(K, N + 1):
            dp[i] = 1.0
        for i in range(K - 1, -1, -1):
            #dp[i] = sum(dp[(i + 1):(i + W + 1)]) * 1.0 / W
            if i == K - 1:
                dp[i] = sum(dp[(i + 1):(i + W + 1)]) * 1.0 / W
            else:
                dp[i] = dp[i + 1] - dp[i + W + 1] * 1.0 / W + dp[i + 1] * 1.0 / W
        #print dp
        return dp[0]
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float