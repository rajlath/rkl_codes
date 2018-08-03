class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        f = [0,1]
        for i in range(2,n):
            f.append(f[i-1] + f[i-2])
        return f[-1]

sol = Solution()
print(sol.fibonacci(7))

