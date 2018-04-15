#include <bits/stdc++.h>
using namespace std;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long ll;

const ll MOD=1000000000 + 7;

map<int, int> square_free;
set<int> memo;

void get_factor(int n) {
    int m = n;
    for (int i = 2; i <= n; i++) {
        if (i > m) break;
        if (i * i > n) break;
        if (m % i == 0) {
            while (m % i == 0) m /= i;
            if (n / i > 1)
                gen_square_free(n / i);
            if ((n / i) % i != 0) {
                if (n / i > 1) {
                    if (square_free.find(n / i) != square_free.end()) {
                        square_free[n] = square_free[n / i] * -1;
                    }
                } else {
                    square_free[n] = -1;
                }
            }
        }
    }
    if (m > 1) {
        square_free[n] = -1;
    }
}

ll pmd(int a, int b, int c) {
    ll ret = 1;
    while (b) {
        if (b&1) {
            ret = (ret * a) % c;
        }
        b >>= 1;
        a = ((ll)a * a) % c;
    }
    return ret;
}

map<int, ll> M;

ll Q(int n, int k) {
    if (M.find(n) != M.end()) {
        return M[n];
    }
    ll tot = pmd(k, n, MOD);
    for (map<int, int>::iterator it= square_free.begin(); it != square_free.end(); it++) {
        int num = it->fs;
        int op = it->sc;
        if (num > n) break;
        if (n % num == 0) {
            ll tmp = pmd(k, n / num, MOD);
            tot = (tot + tmp * op + MOD) % MOD;
        }
    }
    return M[n] = tot;
}

int main()
{
    int n, k;
    cin >> n >> k;
    ll ret = 0;
    square_free.clear();
    memo.clear();
    gen square_free(n);
    M.clear();
    range(i, n + 1) {
         if (i == 0) continue;
         if (n % i == 0) {
             int x = i;
             int y = n / i;
             if (x > y) break;
             ret = (ret + (ll)Q(x, k) * x % MOD) % MOD;
             if (x != y)
                 ret = (ret + (ll)Q(y, k) * y % MOD) % MOD;
         }
     }
     cout<<ret ;
     return (0)

}

