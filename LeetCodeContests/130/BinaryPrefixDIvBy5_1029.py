class Solution:
    def baseNeg2(self, N):
        if N == 0: return "0"
        rets = ''
        while N != 0:
            reminder = N % (-2)
            N //= (-2)
            if reminder < 0:
                reminder += 2
                N += 1
            rets = str(reminder) + rets
        return rets


print(Solution().baseNeg2(3))