'''
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
'''

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([1 for x in S if x in J])

sol = Solution()
print(sol.numJewelsInStones(J = "z", S = "ZZ"))