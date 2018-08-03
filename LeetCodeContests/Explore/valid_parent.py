class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = "({["
        r = ")}]"
        stk = []
        for i in s:
            if i in l:stk.append(i)
            else:
                if len(stk) == 0 or i != r[l.index(stk.pop())]:
                    return False
        return stk == []

print(Solution().isValid("]"))