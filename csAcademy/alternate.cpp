#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n; cin >> n;
    vector<int> els(2 * n);
    int cost = 1e9;
    for (auto& itr : els) {
        cin >> itr;
    }

    for (int t = 0; t < 2; t += 1) {
        int current_cost = 0;
        for (int i = 0; i < 2 * n; i += 1) {
            if (els[i] != (i & 1)) {
                current_cost += 1;
            }
        }
        cost = min(cost, current_cost);
        reverse(els.begin(), els.end());
    }

    cout << cost / 2 << '\n';
    return 0;
}