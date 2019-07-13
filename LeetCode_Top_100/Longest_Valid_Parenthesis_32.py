class Solution:
    def longestValidParentheses(self, s: str) -> int:
        S = []
        max_len = 0
        S.append(-1)
        for i, v in enumerate(s):
            if v == "(":
                S.append(i)
            else:
                S.pop()
                if len(S) == 0:
                    S.append(i)
                else:
                    max_len = max(max_len, i - S[-1])
            print(S)
        return max_len

print(Solution().longestValidParentheses("(()"))
