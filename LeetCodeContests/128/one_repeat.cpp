/* solution by waakaaka*/
#include <bits/stdc++.h>
using namespace std;
#define db(x) cerr << #x << "=" << x << endl
#define db2(x, y) cerr << #x << "=" << x << "," << #y << "=" << y << endl
#define db3(x, y, z) cerr << #x << "=" << x << "," << #y << "=" << y << "," << #z << "=" << z << endl
#define dbv(v) cerr << #v << "="; for (auto _x : v) cerr << _x << ", "; cerr << endl
#define dba(a, n) cerr << #a << "="; for (int _i = 0; _i < (n); ++_i) cerr << a[_i] << ", "; cerr << endl
typedef long long ll;
typedef long double ld;
class Solution {
public:
    int n;
    int dis;
    void go(ll val, int bs) {
        if (val <= n) ++dis;
        if (val * 10 > n) return;
        for (int i = 0; i <= 9; ++i) {
            if (!bs && i == 0) continue; // no 0 for first digit
            if (bs & (1 << i)) continue;
            go(val * 10 + i, bs | (1 << i));
        }
    }
int numDupDigitsAtMostN(int N) {
    dis = 0;
    n = N;
    go(0, 0);
    return N + 1 - dis;
}
};