class Solution(object):
    def removeDuplicates(self, S, K):
        stack = []
        for c in S:
            if not stack:
                stack.append([c, 1])
            elif stack[-1][0] != c:
                stack.append([c, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        return "".join(c*t for c, t in stack)

print(Solution().removeDuplicates())

