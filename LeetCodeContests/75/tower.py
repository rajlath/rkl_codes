class Solution(object):
    def champagneTower(self, poured, i, j):
        arr = [[0 for _ in range(i+1)] for _ in range(i+1)]
        arr[0][0] = poured
        for i1 in range(1, i+1):
            for j1 in range(i1+1):
                print(j1)
                if j1:
                    arr[i1][j1] += max(arr[i1-1][j1-1] - 1, 0) / 2.0
                if j1 < i1:
                    arr[i1][j1] += max(arr[i1-1][j1] - 1, 0) / 2.0
        return min(arr[i][j], 1.0)

sol = Solution()
print(sol.champagneTower(5,2,2))