class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = list(bin(n)[2:])
        last = n[0]
        for i in range(1, len(n)):
            if last != n[i]:
                last = n[i]
            else:
                return False
        return True

sol = Solution()
print(sol.hasAlternatingBits(11))