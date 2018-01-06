/*
You are given an array a consisting of n integers. You have to process q queries to this array; each query is given as four numbers l, r, x and y, denoting that for every i such that l ≤ i ≤ r and ai = x you have to set ai equal to y.

Print the array after all queries are processed.

Input
The first line contains one integer n (1 ≤ n ≤ 200000) — the size of array a.

The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 100) — the elements of array a.

The third line contains one integer q (1 ≤ q ≤ 200000) — the number of queries you have to process.

Then q lines follow. i-th line contains four integers l, r, x and y denoting i-th query (1 ≤ l ≤ r ≤ n, 1 ≤ x, y ≤ 100).

Output
Print n integers — elements of array a after all changes are made.

Example
input
5
1 2 3 4 5
3
3 5 3 5
1 5 5 1
1 5 1 5
output
5 2 5 4 5
*/
#include<bits/stdc++.h>
#define fi first
#define se second
using namespace std;
typedef unsigned long long LL;
typedef pair<int, int> P;

const int maxn = 200000 / 64 + 5;
LL f[101][maxn];

void Or(LL a[], LL b[], int l, int r) {
    int ll = l >> 6, rr = r >> 6;
    int dl = l & 63, dr = (r & 63) ^ 63;
    LL lx = (b[ll] >> dl) << dl, rx = (b[rr] << dr) >> dr;
    if(ll == rr) {
        lx &= rx;
        a[ll] |= lx;
        b[ll] ^= lx;
    } else {
        a[ll] |= lx;
        b[ll] ^= lx;
        a[rr] |= rx;
        b[rr] ^= rx;
        for(int i = ll + 1; i < rr; i++) {
            a[i] |= b[i];
            b[i] = 0;
        }
    }
}

int main() {
#ifdef CX_TEST
    freopen("E:\\program--GG\\test_in.txt", "r", stdin);
#endif
    int n, q, i, j, x, y, l, r;
    scanf("%d", &n);
    for(i = 1; i <= n; i++) {
        scanf("%d", &x);
        f[x][i >> 6] |= 1uLL << (i & 63);
    }
    scanf("%d", &q);
    while(q--) {
        scanf("%d%d%d%d", &l, &r, &x, &y);
        Or(f[y], f[x], l, r);
    }
    for(i = 1; i <= n; i++) {
        for(j = 1; j <= 100; j++) {
            if((f[j][i >> 6] >> (i & 63)) & 1) break;
        }
        printf("%d%c", j, " \n"[i == n]);
    }
    return 0;
}