
a = []
n, m = [int(x) for x in input().split()]
b = [[0 for x in range(m+1)] for y in range(n+1)]
c = [[0 for x in range(m+1)] for y in range(n+1)]

for i in range(n):
    a.append([0]+[int(x) for x in input().split()]+[0])

ans = 0
for i in range(n, 0, -1):
    for j in range(1, m+1):
        if a[i][j]:
            b[i][j] = b[i][j-1] + 1
            c[i][j] = c[i+1][j] + 1
            if b[i][j] > 1 and c[i][j] > 1:
                ans = max(ans, b[i][j] + c[i][j] - 1)
        else:
            b[i][j] = 0
            c[i][j] = 0
print(ans)            
 
    
    
'''    
#include <iostream>
using namespace std;

int a[305][305];
int b[305][305];
int c[305][305];

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= n; ++ i) {
        for (int j = 1; j <= m; ++ j) {
            cin >> a[i][j];
        }
    }
    int ans = 0;
    for (int i = n; i >= 1; -- i) {
        for (int j = 1; j <= m; ++ j) {
            if (a[i][j]) {
                b[i][j] = b[i][j - 1] + 1;
                c[i][j] = c[i + 1][j] + 1;
                if (b[i][j] > 1 && c[i][j] > 1) {
                    ans = max(ans, b[i][j] + c[i][j] - 1);
                }
            } else {
                b[i][j] = c[i][j] = 0;
            }
        }
    }
    cout << ans;
    return 0;
}    
'''    
    

    
  
    
    
    
