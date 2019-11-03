class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        d = lambda x: abs(ord(s[x]) - ord(t[x]))
        n = len(s)
        c = 0
        r = 0
        for i in range(n):
            c += d(i)
            if c > maxCost:
                c -= d(i - r)
            else:
                r += 1
        return r

print(Solution().equalSubstring("abcd", "bcdf", 3))
