#include <bits/stdc++.h>
using namespace std;


int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr), cout.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    int mn = *min_element(a.begin(), a.end());
    int sum = accumulate(a.begin(), a.end(), 0);
    cout << sum << endl;
    int res = sum;
    for(int i = 0; i < n; ++i) {
        for(int d = 1; d <= a[i]; ++d) {
            if (a[i] % d != 0) continue;
            int cur = sum - mn - a[i];
            cur += mn * d + a[i] / d;
            res = min(res, cur);
        }
    }
    cout << res << endl;

    return 0;
}