#include<bits/stdc++.h>
using namespace std;
int main()
{ 
    int n;
    cin>>n; 
    int a[n+1],g[n+1];
    for(int i=1;i<=n;i++)
     { 
         cin>>a[i];
         g[i]=0;
     }
     g[0] = 0;
     int q;
     cin>>q;
     int l,r;
     while(q--)
     { 
         cin>>l>>r;
         g[l] += 1; 
         g[r+1] -= 1;
     }
     for(int i=1;i<=n;i++) 
        g[i] = (g[i]+g[i-1]); 
     for(int i=1;i<=n;i++)
     { 
        if(g[i]%2==1)
        { 
            swap(a[i],a[n-i+1]);
        }
     } 
     for(int i=1;i<=n;i++)
        cout<<a[i]<<" ";
}
