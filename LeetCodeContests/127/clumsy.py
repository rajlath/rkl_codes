class Solution:
    def clumsy(self, N: int) -> int:
        ops = ["*", "//", "+", "-"]
        eqs = []
        indx= 0
        for i in range(N, 0, -1):
            eqs.append(str(i))
            if i == 1:break
            eqs.append(ops[indx])
            indx += 1
            if indx == 4:indx = 0
        return eval(''.join(eqs))

print(Solution().clumsy(10))

class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = []
        o = ['*', '//', '+', '-']
        k = 0
        for i in range(N, 0, -1):
            s.append(str(i))
            s.append(o[k])
            k = (k + 1) % 4
        s.pop()
        return eval(''.join(s))