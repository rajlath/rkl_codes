'''
class Solution {
public:
    int up[501], down[501][501], right[501][501];
    int a[501][501];

    int orderOfLargestPlusSign(int N, vector<vector<int>>& mines) {
        memset(a, 0, sizeof(a));
        for (int i = 0;i < mines.size();++i)
            a[mines[i][0]][mines[i][1]] = 1;
        memset(down, 0, sizeof(down));
        memset(right, 0, sizeof(right));
        for (int i = N - 1;i >= 0;--i)
            for (int j = N - 1;j >= 0;--j)
                if (a[i][j] == 1) right[i][j] = down[i][j] = 0;
                else {
                    right[i][j] = down[i][j] = 1;
                    if (i < N - 1) down[i][j] += down[i + 1][j];
                    if (j < N - 1) right[i][j] += right[i][j + 1];
                }
        int res = 0;
        memset(up, 0, sizeof(up));
        for (int i = 0;i < N;++i) {
            int left = 0;
            for (int j = 0;j < N;++j) {
                if (a[i][j] == 1) up[j] = 0;
                else up[j] += 1;
                if (a[i][j] == 1) left = 0;
                else left += 1;
                res = max(res, min(min(up[j], down[i][j]), min(left, right[i][j])));
            }
        }
        return res;
    }
};

'''

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """

        a     = [[0 for x in range(N)] for y in range(N)]
        right = [[0 for x in range(N)] for y in range(N)]
        down  = [[0 for x in range(N)] for y in range(N)]
        up    = [0 for y in range(N)]


        for i in range(len(mines)):
            a[mines[i][0]][mines[i][1]] = 1
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if a[i][j] :
                    right[i][j] = down[i][j] = 0
                else:
                    right[i][j] = down[i][j] = 1
                    if (i < N - 1): down[i][j] += down[i + 1][j]
                    if (j < N - 1): right[i][j] += right[i][j + 1]
        res = 0
        for i in range(N):
            ileft = 0
            for j in range(N):
                if a[i][j] == 1:
                    up[j] = 0
                    ileft  = 0
                else:
                    up[j] += 1
                    ileft  += 1
                res = max(res, min(min(up[j], down[i][j]), min(ileft, right[i][j])))

        return res







sol = Solution()
print(sol.orderOfLargestPlusSign(2, []))

