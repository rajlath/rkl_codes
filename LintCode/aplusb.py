class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here

        while (b != 0):
            carry = a & b
            a = a ^ b
            if carry: b = carry << 1
        return a


sol = Solution()
print(sol.aplusb(100, -100))