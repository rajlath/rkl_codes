'''
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, s, d;
    cin >> n >> s >> d;
    vector<int> v(n+1);
    for (int i = 1; i <= n; ++i)
        cin >> v[i];
    int p = s;
    int ans = 0;
    int flag = 1, count = n;
    while (p != d) {
        if (count == 0) {
            flag = 0;
            break;
        }
        count--;
        p = v[p];
        ++ans;
    }
    if (flag)
        cout << ans << '\n';
    else
        cout << "-1\n";
}
