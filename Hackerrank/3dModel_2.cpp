using namespace std;
#include <bits/stdc++.h>
#define maxn 105  

int surfaceArea(vector < vector<int> > A, int m, int n) {
    int arr[maxn][maxn];  
    int flag[maxn][maxn]; 
    int ud=0,max=0; 
   
    for(int i=1; i<=m; i++)  
    {
        for(int j=1; j<=n; j++)  
        {
            char temp; 
            //cin>>temp;
            temp = A.at(i-1).at(j-1);
            arr[i][j]=temp-'0';  
            if(arr[i][j]>0) ud++;  
            max=max>arr[i][j]?max:arr[i][j];
            
        }
        
    }
   
    long long sum=2*ud;  
        for(int i=0; i<max; i++)  
        {  
            memset(flag,0,sizeof(flag));  
            for(int i=1; i<=m; i++)  
                for(int j=1; j<=n; j++)  
                    if(arr[i][j]>0) flag[i][j]=1;  
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
        cout<<sum;            
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
