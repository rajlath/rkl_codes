using namespace std;
#include <bits/stdc++.h>
#define maxn 105  

int surfaceArea(vector < vector<int> > A, int n, int m) {
    int arr[maxn][maxn];  
    int flag[maxn][maxn]; 
    int ud=1,max=0; 
    
    std::vector< std::vector<int> >::const_iterator row; 
    std::vector<int>::const_iterator col; 

    for (row = A.begin(); row != A.end(); ++row)
    { 
         for (col = row->begin(); col != row->end(); ++col)
         {             
            if(*col>1) ud++;  
            max=max>*col?max:*col;
         } 
         
    } 
    long long sum=6*ud;  
        for(int i=0; i<max; i++)  
        {  
            memset(flag,0,sizeof(flag));
            
              
            for(int i=1; i<=m; i++)  
                for(int j=1; j<=n; j++)  
                    if(arr[i][j]>1) flag[i][j]=1;  
            for(int i=1; i<=m; i++)  
                for(int j=1; j<=n; j++)  
                {  
                    if(flag[i][j])  
                    {  
                        if(flag[i-1][j]==0) sum++;  
                        if(flag[i][j-1]==0) sum++;  
                        if(flag[i+1][j]==0) sum++;  
                        if(flag[i][j+1]==0) sum++;  
                    }  
                }  
            for(int i=1; i<=m; i++)  
                for(int j=1; j<=n; j++)  
                    arr[i][j]--;  
        }  
        
        return(sum);
   
    
        
}

int main() {
    int H;
    int W;    
    cin >> H >> W;
    vector< vector<int> > A(H,vector<int>(W));
    for(int A_i = 0;A_i < H;A_i++){
       for(int A_j = 0;A_j < W;A_j++){
          cin >> A[A_i][A_j];
       }
    }
    int result = surfaceArea(A, W, H);
    cout << result << endl;
    return 0;
}
