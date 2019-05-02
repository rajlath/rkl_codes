class Solution:
    def removeOuterParentheses(self, S):
        balance = 0
        rets = ''
        curr = ''
        for i, p in enumerate(S):
            curr += p
            balance += [-1, 1][p == "("]
            if balance == 0:
                rets += curr[1:-1]
                curr = ''
        return rets

print(Solution().removeOuterParentheses("(()())(())"))

