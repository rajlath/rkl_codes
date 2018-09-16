#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int n, m, k, x, y, s;
queue<int> qu, qx, qy;
char a[1005][1005];
int main() {
    int i, tx, ty, tu;
    cin >> n >> m >> k;
    for (i = 1; i <= n; i++) {
        scanf("%s", &a[i][1]);
    }
    while (k--) {
        scanf("%d %d", &x, &y);
        qx.push(x);
        qy.push(y);
        qu.push(0);
    }
    while (!qx.empty()) {
        tx = qx.front(); qx.pop();
        ty = qy.front(); qy.pop();
        tu = qu.front(); qu.pop();
        if (a[tx][ty] == '.') {
            s += tu;
            a[tx][ty] = ' ';
            qx.push(tx + 1); qy.push(ty); qu.push(tu + 1);
            qx.push(tx - 1); qy.push(ty); qu.push(tu + 1);
            qx.push(tx); qy.push(ty + 1); qu.push(tu + 1);
            qx.push(tx); qy.push(ty - 1); qu.push(tu + 1);
        }
    }
    cout << s;
    return 0;
}
    cout << a + b;
}