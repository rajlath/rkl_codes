class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:return []
        triange = [0, 1, 0]
        res = [triange[1:-1]]
        for i in range(numRows-1):
            rows = []
            for j in range(1, len(triange)):
                rows.append(triange[j] + triange[j-1])
            triange = [0] +rows[:] +[0]
            res.append(triange[1:-1])
        return res




print(Solution().generate(5))
