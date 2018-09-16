/**
 *    author:  tourist
 *    created: 14.07.2018 20:05:56
**/
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<vector<int>> a(n, vector<int>(n, -1));
  for (int num = 0; num < n; num++) {
    for (int i = 0; i < (n + 1) / 2; i++) {
      a[(i + num) % n][num] = num;
    }
    for (int j = 0; j < n / 2 + 1; j++) {
      a[num][(j + num) % n] = num;
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        cout<<a[i][j]<<" ";
    cout<<"\n";
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (j > 0) {
        cout << ' ';
      }
      cout << a[i][j] + 1;
    }
    cout << '\n';
  }
  return 0;
}