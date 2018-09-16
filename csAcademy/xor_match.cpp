#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


int main() {
    int n, m; cin >> n >> m;
    vector<int> a(n), b(m);
    for (auto& itr : a) { cin >> itr; }
    for (auto& itr : b) { cin >> itr; }

    int answer = 0;
    for (int start = 0; start + a.size() <= b.size(); start += 1) {
        bool ok = true;
        for (int offset = 0; offset < (int)a.size(); offset += 1) {
            ok &= a[offset] ^ (b[start + offset]);
        }

        answer += ok;
    }

    cout << answer << '\n';

    return 0;
}
