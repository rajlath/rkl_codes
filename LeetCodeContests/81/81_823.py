class Solution(object):
    def numFactoredBinaryTrees(self, A):
        from collections import defaultdict

        d = set(A)

        f = defaultdict(list)
        for i in range(len(A)):
            if A[i] * A[i] in d:
                f[A[i] * A[i]].append((A[i], A[i]))
            for j in range(i+1, len(A)):
                if A[i] * A[j] in d:
                    f[A[i] * A[j]].append((A[i], A[j]))
                    f[A[i] * A[j]].append((A[j], A[i]))

        level = {}
        for x in sorted(A):
            if not f[x]:
                level[x] = 0
            else:
                ans = 0
                for i, j in f[x]:
                    ans = max(ans, level[i], level[j])
                level[x] = ans + 1

        g = {}
        mod = 10 ** 9 + 7
        for x in sorted(A, key=lambda y: level[y]):
            ans = 1
            for i, j in f[x]:
                ans += g[i] * g[j]
            g[x] = ans % mod

        return sum(g[y] for y in A) % mod
