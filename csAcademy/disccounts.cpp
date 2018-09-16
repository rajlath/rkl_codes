#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n, v; cin >> n >> v;
    vector<pair<int, int>> discounts(n);
    for (auto& itr : discounts) {
        cin >> itr.first >> itr.second;
    }

    sort(discounts.begin(), discounts.end());

    int mn = v;
    int discounted = 0;

    for (auto itr : discounts) {
        discounted += itr.second;
        if (itr.first > v) {
            mn = min(mn, itr.first - discounted);
        } else {
            mn = min(mn, v - discounted);
        }
    }

    cout << mn << '\n';
    return 0;
}
