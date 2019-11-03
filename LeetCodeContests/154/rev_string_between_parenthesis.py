class Solution:
    def reverseParentheses(self, s):
        stack = [[]]
        for i in s:
            if i == "(":
                stack.append([])
            elif i == ")":
                curr = stack.pop()
                for x in reversed(curr):
                    stack[-1].append(x)
                #print(stack)
            else:
                stack[-1].append(i)
        return "".join(stack[-1])

print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))