class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = [False]*len(s)
        h = 0
        t = []
        for i, c in enumerate(s):
            if c == '(':
                t.append(i)
            elif c == ')':
                if t: t.pop()
                else: r[i] = True
        while t:
            r[t.pop()] = True
        return ''.join(c for i,c in enumerate(s) if not r[i])