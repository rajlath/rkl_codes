class Solution:
    def bitwiseComplement(self, N: int) -> int:
        comp = ''
        bins = bin(N)[2:]
        for c in range(len(bins)):
            comp += '1' if (bins[c] == '0') else '0'
        return int(comp, 2)

#solution by wangfeg1027

class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        s = s.replace('1','2').replace('0','1').replace('2','0')
        return int(s,2)