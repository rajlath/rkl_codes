#include<bits/stdc++.h>
using namespace std;
#define ll long long
// Driver program
int main()
{
    ll n;
    cin>>n;
    ll a[n];
    for(ll i=0;i<n;i++)
        cin>>a[i];
    ll pre[n+1];
    pre[0]=0;
    for(ll i=0;i<n;i++)
        pre[i+1]=pre[i]+a[i];
    set<ll>s;
    for(ll i=1;i<=n;i++)
        for(ll j=i;j<=n;j++)
            s.insert(pre[j]-pre[i-1]);
        cout<<s.size()<<endl;


}