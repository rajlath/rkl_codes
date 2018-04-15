'''
693. Binary Number with Alternating Bits
User Accepted: 1873
User Tried: 1986
Total Accepted: 1929
Total Submissions: 4203
Difficulty: Easy
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have
different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nb  = bin(n)[2:]
        last= nb[0]
        for i in nb[1:]:
            if i == last:
                return False
            last = i
        return True
sol = Solution()
print(sol.hasAlternatingBits(5))
