ox[4] = [0, 0, -1, 1]
oy[4] = [-1, 1, 0, 0]
def dfs(x, y, n):
    if x == n -1 and x == y:cnt+=1
    else:
        for i in range(4):
            if is_ok(x+ox[i], y+oy[i]) and not m[x+ox[i][y+y[i]]]:


void dfs(int x, int y) {
    if(x == n-1 && x == y) {
        cnt++;
    } else {
        for(int i = 0; i < 4; i++) {
            if(isOK(x+ox[i], y+oy[i]) && !m[x+ox[i]][y+oy[i]]) {
                m[x+ox[i]][y+oy[i]] = 1;
                dfs(x+ox[i], y+oy[i]);
                m[x+ox[i]][y+oy[i]] = 0;
            }
        }
    }
}

for _ in range(int(input())):
    nor = int(input())
    for i in range(n):
        a.append([int(x) for x in input().split()])
        m.append([0 for x in range(n)])
    cnt = 0
    m[0][0] = 1
    cnt = dfs(0, 0)
    print(cnt)




#include <cstring>
#include <stack>
using namespace std;
typedef long long int Long;

char a[21][21], m[21][21];
int t, n, tmp, cnt,
    ox[4] = {0, 0, -1, 1},
    oy[4] = {-1, 1, 0, 0};

inline int isOK(int x, int y) { return (x >= 0 && y >= 0 && x < n && y < n && !a[x][y]); }


    }

    return 0;
}
'''