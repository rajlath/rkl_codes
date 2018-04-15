'''
#include <bits/stdc++.h>
using namespace std;
const int maxn = 501, INF = 0x3f3f3f3f;
int n, m, q, f[maxn], g[maxn], tot, seq[maxn];
char buf[maxn];
int main() {
	scanf("%d%d%d", &n, &m, &q);
	while(n--) {
		scanf("%s", buf);
		tot = 0;
		for(int i = 0; i < m; ++i)
			if(buf[i] == '1')
				seq[tot++] = i;
		for(int i = 0; i < tot; ++i) {
			g[i] = INF;
			for(int j = 0, k = tot - 1 - i; k < tot; ++j, ++k)
				g[i] = min(g[i], seq[k] - seq[j] + 1);
		}
		g[tot] = 0;
		for(int i = q; i >= 0; --i) {
			f[i] += g[0];
			for(int j = 1; j <= tot && j <= i; ++j)
				f[i] = min(f[i], f[i - j] + g[j]);
		}
	}
	printf("%d\n", f[q]);
	return 0;
}
'''
maxs = int( 0x3f3f3f3f)
series = [0] * 501
g  = [maxs] * 501
f  = [maxs] * 501
n, m , q = [int(x) for x in input().split()]
for i in range(n):
    s = input()
    cnt = 0
    for i, v in enumerate(s):
        if  v ==  "1":
            cnt += 1
            series[cnt] = i+1
    g[0] = series[cnt] - series[1] + 1;
    j = 1
    while j <= min(cnt, k):
        k1 = cnt - j
        while k1 <= cnt:
            k1 += 1
            g[j] = min(g[j], series[k] - series[k - (cnt - j) + 1] + 1)

    if (cnt <= k):

			help[cnt] = 0;
		for (int j = 0; j <= k; ++j) {
			dp[i][j] = dp[i - 1][j] + help[0];
			for (int l = 1; l <= min(j, cnt); ++l)
				dp[i][j] = min(dp[i][j], dp[i - 1][j - l] + help[l]);
		}


