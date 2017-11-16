
#include <stdio.h>  
#include <memory.h> 
using namespace std;
#include <bits/stdc++.h> 
#define maxn 105  
  

int main()  
{  
    int arr[maxn][maxn],m,n;  
    int flag[maxn][maxn];  
    cin>>m>>n;    
    int ud=0,max=0; 
    for(int i=1; i<=m; i++)  
    {
        for(int j=1; j<=n; j++)  
        {
            char temp; 
            cin>>temp;
            arr[i][j]=temp-'0';  
            if(arr[i][j]>0) ud++;  
            max=max>arr[i][j]?max:arr[i][j];
            
        }
        
    }
        
        long long sum=2*ud;  
        for(int i=0; i<max; i++)  
        {  
            memset(flag,0,sizeof(flag));  
            for(int i=1; i<=n; i++)  
                for(int j=1; j<=m; j++)  
                    if(arr[i][j]>0) flag[i][j]=1;  
            for(int i=1; i<=n; i++)  
                for(int j=1; j<=m; j++)  
                {  
                    if(flag[i][j])  
                    {  
                        if(flag[i-1][j]==0) sum++;  
                        if(flag[i][j-1]==0) sum++;  
                        if(flag[i+1][j]==0) sum++;  
                        if(flag[i][j+1]==0) sum++;  
                    }  
                }  
            for(int i=1; i<=n; i++)  
                for(int j=1; j<=m; j++)  
                    arr[i][j]--;  
        }  
        printf("%lld\n",sum);
        return(0);  
    }  
    
