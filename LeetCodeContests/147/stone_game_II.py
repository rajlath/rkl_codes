class Solution:
    def stoneGameII(self, piles):

        def f(p, m):
            if p >= n:
                return 0
            if p + m >= n:
                return s[p]
            if (p, m) in memo:
                return memo[(p, m)]
            ret = float('-inf')
            for i in range(1, 2 * m + 1):
                ret = max(ret, -f(p + i, max(i, m)))
            ret += s[p]
            memo[(p, m)] = ret
            return ret

        memo = dict()
        n = len(piles)
        s = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] + piles[i]
        return f(0, 1)
print(Solution().stoneGameII([2,7,9,4,4]))
