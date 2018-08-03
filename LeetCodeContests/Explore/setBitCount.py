class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result

print(Solution().hammingWeight(122))