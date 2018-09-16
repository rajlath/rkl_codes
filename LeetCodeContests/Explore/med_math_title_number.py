'''
Given a column title as appear in an Excel sheet,
return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
from string import ascii_uppercase as uc
alpha = dict(zip(uc, list(range(1, 27))))
from string import ascii_uppercase as uc
alpha = dict(zip(uc, list(range(1, 27))))
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for c in s:
            if c in uc:
                num = num * 26 + alpha[c]
        return num

print(Solution().titleToNumber("AAA"))