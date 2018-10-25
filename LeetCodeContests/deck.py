from collections import Counter
from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        deckc = Counter(deck)
        counts= deckc.values()
        gc_d = 0
        for c in counts:
            gc_d = gcd(gc_d, c)
        return gc_d != 1


print(Solution().hasGroupsSizeX([0,0,0,1,1,1,1,1,1,2,2,2,3,3,3]))