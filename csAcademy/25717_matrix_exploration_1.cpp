#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

#define maxN 1011
#define mp make_pair

const int defX[4] = {0, 0, -1, 1};
const int defY[4] = {-1, 1, 0, 0};

int n, m, i, j, k, x, y;
char mat[maxN][maxN];
int dp[maxN][maxN];
queue< pair<int, int> > Q;

long long ans;

int main() {
    scanf("%d%d%d\n", &n, &m, &k);
    for (i = 1; i <= n; i++)
        scanf("%s\n", mat[i] + 1);
    for (i = 1; i <= k; i++) {
        scanf("%d%d", &x, &y);
        Q.push(mp(x, y));
        dp[x][y] = 1;
    }

    while (!Q.empty()) {
        auto pos = Q.front(); Q.pop();

        for (i = 0; i < 4; i++) {
            int xx = pos.first + defX[i];
            int yy = pos.second + defY[i];
            
            if (xx < 1 || xx > n || yy < 0 || yy > m) continue;
            if (mat[xx][yy] != '.') continue;
            if (dp[xx][yy] != 0) continue;

            dp[xx][yy] = dp[pos.first][pos.second] + 1;
            Q.push(mp(xx, yy));
        }
    }

    for (i = 1; i <= n; i++)
        for (j = 1; j <= m; j++)
            if (dp[i][j] > 0)
                ans += dp[i][j] - 1;

    printf("%lld", ans);

}
