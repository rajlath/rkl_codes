#include <bits/stdc++.h>

using namespace std;

int matrixLand(vector < vector<int> > A) {
    int result = 0 ;
    int rows = A.size();
    int cols = A[0].size();
    
    int dp[cols][rows+2];
    memset(dp, 0, sizeof(dp));
    
    for (int i = 0 ; i < cols ; i++)
        dp[0][i+1] = A[0][i];
        
    for (int i = 1 ; i < rows ; i++)
        for (int j = 1 ; j <= cols ; j++)
        {
            dp[i][j] = max(dp[i-1][j-1],max(dp[i-1][j],dp[i-1][j+1])) +  A[i][j-1] ; 
            
        }
                       
    result = max(result, dp[rows-1][cols -1]);
    return result ;                      
    
    
   
    
    
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector< vector<int> > A(n,vector<int>(m));
    for(int A_i = 0;A_i < n;A_i++){
       for(int A_j = 0;A_j < m;A_j++){
          cin >> A[A_i][A_j];
       }
    }
    int result = matrixLand(A);
    cout << result << endl;
    return 0;
}

