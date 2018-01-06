'''
738. Monotone Increasing Digits My SubmissionsBack to Contest

Difficulty: Medium
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy
x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
'''
class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = '0' + str(N)
        n = len(N)
        prefix = '0'
        while len(prefix) < n:
            # Decide what to add next
            for ch in '9876543210':
                candidate = prefix + ch * (n - len(prefix))
                if candidate <= N:
                    prefix += ch
                    break
        return int(prefix)

sol = Solution()
sol.monotoneIncreasingDigits(332)