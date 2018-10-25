from itertools import groupby
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        ngrp = [list(g) for k, g in groupby(name)]
        tgrp = [list(g) for k, g in groupby(typed)]
        for i, x in enumerate(ngrp):
            if i > len(tgrp)-1 or tgrp[i][0] != x[0] or len(tgrp[i]) < len(x):
                return False
        return True

print(Solution().isLongPressedName("pyplrz","ppyypllr"))



