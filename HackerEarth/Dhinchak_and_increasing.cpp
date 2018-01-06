#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;cin>>t;
    while(t--)
    {
        int n;cin>>n;
        vector<int> a(n+2);
        vector<int> pre(n+2),suf(n+2);
        for(int i=1;i<=n;i++)
            cin>>a[i];
        a[0]=INT_MIN;a[n+1]=INT_MAX;
        for(int i=1;i<=n;i++)
            if(a[i]>a[i-1]) pre[i]=pre[i-1]+1;
            else pre[i]=1;
        for(int i=n;i>=1;i--)
            if(a[i]<a[i+1]) suf[i]=suf[i+1]+1;
            else suf[i]=1;
        int ans=0;
        for(int i=1;i<=n;i++)
        {

            if(a[i+1]-a[i-1]>=2&&!(a[i]>a[i-1]&&a[i]<a[i+1]))
            {ans=max(ans,pre[i-1]+suf[i+1]+1);}
            else ans=max(ans,max(pre[i-1]+1,suf[i+1]+1));

        }
        cout<<ans<<endl;
    }
}