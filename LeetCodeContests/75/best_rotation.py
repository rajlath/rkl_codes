class Solution(object):
    def bestRotation(self, A):
        points = [0 for _ in A]
        n = len(A)
        sc = sum(1 for i, x in enumerate(A) if i >= x)
        ans = 0
        print(sc)
        for i, x in enumerate(A):
            if not x: continue
            if x <= i:
                points[i - x + 1] -= 1
            else:
                points[(i + n - x + 1)%n] -= 1
            points[(i+1) % n] += 1
        res = sc
        print(points)
        for k in range(1, n):
            res += points[k]
            if res > sc:
                sc = res
                ans = k
        return ans

sol = Solution()
print(sol.bestRotation([2, 3, 1, 4, 0]))