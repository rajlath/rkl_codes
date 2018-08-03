'''
859. Buddy Strings

Difficulty: Easy
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A
so that the result equals B.
Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
'''
from collections import Counter
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        AC = Counter(A)
        BC = Counter(B)
        if AC != BC: return False
        sums =  sum([1 for a, b in zip(A,B) if a != b])
        if sums == 2:return True
        return A == B and any(v>=2 for v in AC.values())

sol = Solution()
print(sol.buddyStrings("aa", "aa"))