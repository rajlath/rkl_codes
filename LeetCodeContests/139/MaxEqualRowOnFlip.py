class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """"
        :param matrix type :List(Int)
        :rtype: int
        """
        s = dict()
        for row in matrix:
            first = "".join(map(str, row))
            second= "".join(map(lambda x: str(1 - x), row))
            if first in s:
                s[first]+= 1
            else:s[first] = 1
            if second in s:
                s[second] += 1
            else:
                s[second] = 1
        print(s)
        return max(s.values())
