#include <cstdio>
const long c = 1000000007;
int main(){
  int n,m,r,x,y,v;
  scanf("%d %d",&n,&m);
  int A[n][m];
  long B[n][m];
  for(int i = 0; i < n; ++i){
    for(int j = 0; j < m; ++j){
      A[i][j] = B[i][j] = 0;
    }
  }
  scanf("%d",&r);
  for(int i = 0; i < r; ++i){
    scanf("%d %d %d",&x,&y,&v);
    A[x][y] = v;
  }
  B[0][0] = 1;
  for(int i = 0; i < n; ++i){
    for(int j = 0; j < m; ++j){
      v = A[i][j];
      if(v == -1) continue;
      if(i+1 < n && A[i+1][j] != -1) B[i+1][j] = (B[i+1][j] + B[i][j])%c;
      if(j+1 < m && A[i][j+1] != -1) B[i][j+1] = (B[i][j+1] + B[i][j])%c;
      if(v != 0){
        if(i+v < n && A[i+v][j] != -1) B[i+v][j] = B[i+v][j] + B[i][j];
        if(j+v < m && A[i][j+v] != -1) B[i][j+v] = B[i][j+v] + B[i][j];
      }
    }
  }
  printf("%ld",B[n-1][m-1]);
}