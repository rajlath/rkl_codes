'''
#include <bits/stdc++.h>

using namespace std;

const int mod = 1e9 + 7;

signed main()
{
    //freopen("input.txt", "r", stdin);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k, x;
    cin >> n >> k >> x;
    assert(3 <= n && n <= 100000);
    assert(2 <= k && k <= 100000);
    assert(1 <= x && x <= k);
    int d[n];
    d[0] = 0;
    d[1] = 1;
    for(int i = 2; i < n; i++)
        d[i] = (1LL * (k - 2) * d[i - 1] + 1LL * (k - 1) * d[i - 2]) % mod;
    cout << (x == 1 ? 1LL * (k - 1) * d[n - 2] % mod : d[n - 1]) << endl;
}
761 99 1
236568308
'''
mod = int(1e9 + 7)

n, k, x = [int(x) for x in input().split()]
d = [0]*n
d[0] = 0
d[1] = 1
for i in range(2, n):
    d[i]= (1 * (k - 2) * d[i - 1] + 1 * (k - 1) * d[i - 2]) % mod

if x == 1:
    ans = 1 * (k - 1) * d[n - 2] % mod
else:
    ans = d[n - 1]
print(ans)
