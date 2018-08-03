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
4 2 1
2 3 4 1
'''
n, s, d = [int(x) for x in input().split()]
glasses = [0] + [int(x) for x in input().split()]
tried   = [0] * (n + 1)
ans = -1
moves = 0
if s == d:
    ans = 0
else:
    tried[s] = 1
    moves += 1
    x = glasses[s]
    if not tried[x]:
        tried[x] = 1
    if x == d:
        ans = moves
print(ans)


