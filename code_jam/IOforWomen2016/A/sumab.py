class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        s = a ^ b
        carry = a & b
        if carry == 0: return s
        else:
            return self.aplusb(s, carry << 1)


sol = Solution()
print(sol.aplusb(100, -3))

