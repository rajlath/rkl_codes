class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        uncommon = []
        A = A.split()
        B = B.split()
        for a in A:
            if A.count(a)>1:continue
            if a in B: continue
            else:uncommon.append(a)
        for b in B:
            if B.count(b)>1:continue
            if b in A:continue
            else:uncommon.append(b)
        return uncommon

print(Solution().uncommonFromSentences("d b zu d t","udb zu ap"))
#["b","t","udb","ap"]


class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        z = A.split() + B.split()
        g = {}
        r = []
        for x in z:
            if x in g:
                g[x]+=1
            else:
                g[x] = 1

        for x in z:
            if g[x] ==1:
                r.append(x)
        r.sort()
        return r