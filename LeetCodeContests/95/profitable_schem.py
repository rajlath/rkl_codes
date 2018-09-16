class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # f(g, p) = number of schemes generate exactly p profit using exactly g gang members
        # update to consider crime i:
        # f(g, p) := f(g - group[i], p - profit[i])

        M = 10**9 + 7
        w = [[0 for _ in range(P+1)] for _ in range(G+1)]
        w[0][0] = 1
        for i in range(len(group)):
            for g in range(G - group[i], -1, -1):
                ng = g + group[i]
                for p in range(P, -1, -1):
                    if not w[g][p]: continue
                    np = min(P, p + profit[i])
                    w[ng][np] = (w[ng][np] + w[g][p]) % M
        return sum(w[g][P] for g in range(G+1)) % M

