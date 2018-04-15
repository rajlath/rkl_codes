class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for i in range(1, N+1):
            if any(x for x in str(i) if x in ["3","4","7"]):continue
            if any(x for x in str(i) if x in ["2","5","6","9"]):
                count += 1
        return count

sol = Solution()
print(sol.rotatedDigits(10))