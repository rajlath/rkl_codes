'''
856. Score of Parentheses
Difficulty: Medium
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
'''
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def score(s):
            if s == '':return 0
            if s == '()':return 1
            h = 0
            for i, v in enumerate(s):
                if v == "(": h += 1
                else:
                    h -= 1
                    if h == 0:
                        if i == 1: return 1 + score(s[2:])
                        return 2 * score(s[1:i]) + score(s[i+1:])

        return score(S)

sol = Solution()
print(sol.scoreOfParentheses("(()(()))"))


