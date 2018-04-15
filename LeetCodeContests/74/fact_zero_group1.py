class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        ans = K * 4 // 5
        for i in range(10):
           if self.calc(ans + i) == K:
               return 5
        return 0
    def calc(self, x):
        ans = 0
        while x:
            ans += x
            x //= 5
        return ans



sol = Solution()
print(sol.preimageSizeFZF(5))
