'''
We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
'''
class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        n = len(rectangles)
        x = set()
        y = set()
        for r in rectangles:
            x.add(r[0])
            x.add(r[2])
            y.add(r[1])
            y.add(r[3])
        x = list(sorted(x))
        y = list(sorted(y))
        xt = {j: i for i, j in enumerate(x)}
        yt = {j: i for i, j in enumerate(y)}

        pl = [[0] * (len(x) - 1) for _ in range(len(y) - 1)]
        for r in rectangles:
            for yy in range(yt[r[1]], yt[r[3]]):
                for xx in range(xt[r[0]], xt[r[2]]):
                    pl[yy][xx] = 1
        res = 0
        for yy in range(len(y) - 1):
            for xx in range(len(x) - 1):
                if pl[yy][xx]:
                    res += (y[yy + 1] - y[yy]) * (x[xx + 1] - x[xx])
        return res % (10 ** 9 + 7)

sol = Solution()
print(sol.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))