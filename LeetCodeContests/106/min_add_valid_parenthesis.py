class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        need_more = 0
        for i in S:
            if i == ")":
                if len(stack) ==0:
                    need_more += 1
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    need_more += 1
            else:
                stack.append(i)

        return need_more + len(stack)

print(Solution().minAddToMakeValid("((("))


