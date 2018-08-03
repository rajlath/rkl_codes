class Solution(object):
    def consecutiveNumbersSum(self, n):
        i = 1
        n *= 2
        res = 0
        while i * i <= n:
            if n % i == 0:
                if (n // i - i + 1) % 2 == 0:
                    res += 1
            i += 1
        return res

sol = Solution()
print(sol.consecutiveNumbersSum(10))