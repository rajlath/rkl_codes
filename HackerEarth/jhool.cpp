#include <iostream>
#include <map>
using namespace std;
 
int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    int tc;
    cin >> tc;
    while (tc--) {
        int n, m;
        cin >> n >> m;
        map<int, int> pos;
        bool res = true;
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            if (res) {
                int l = (a <= b ? b - a : b + n - a);
                while (l >= 0 && pos.count(a) == 1) {
                    int r = pos[a];
                    if (r > l) {
                        pos[a] = l;
                        l = r;
                    }
                    ++a;
                    --l;
                    if (a == n)
                        a = 0;
                }
                //cout << a << " " << l << "\n";
                if (l >= 0) {
                    pos[a] = l;
                } else {
                    res = false;
                }
            }
        }
        cout << (res ? "YES\n" : "NO\n");
    }
}

SAMPLE INPUT 
2
4 3
0 1
1 2
2 0
5 5
0 0
1 2
2 3
4 4
4 0
SAMPLE OUTPUT 
YES
NO
