class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ans = ''
        while A and B:
            if A == B:
                ans += "ab"
                A -= 1
                B -= 1
            if A > B:
                ans += "aab"
                A -= 2
                B -= 1
            if A < B:
                ans += "bba"
                A -= 1
                B -= 2

        ans += A * "a"
        ans += B * "b"
        return ans


print(Solution().strWithout3a3b(4, 1))








