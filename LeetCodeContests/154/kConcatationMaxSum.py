# Thanks to awice
class Solution(object):
    def kConcatenationMaxSum(self, A, K):
        def kadane(A):
            max_now, max_all = 0, 0
            for x in A:
                max_now += x
                max_now = max(max_now, x)
                max_all = max(max_all, max_now)
            return max_all
        MOD = 10**9 + 7
        #lens= len(A)
        K1 = kadane(A)
        K2 = kadane(A + A)
        if K == 1:return K1 % MOD
        if K == 2:return K2 % MOD
        sums = sum(A)
        if sums <= 0:return max(K1, K2) % MOD
        base = sums * (K - 2) % MOD
        prefix, suffix = 0, 0
        su = 0
        for x in A:
            su += x
            prefix = max(prefix, su)
        su = 0
        for x in reversed(A):
            su += x
            suffix = max(suffix, su)
        return (base + suffix + prefix) % MOD

print(Solution().kConcatenationMaxSum([1,2],3))


