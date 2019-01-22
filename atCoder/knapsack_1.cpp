#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define int long long int
#define endl "\n"
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

const int N=1e5+5;
int n,a[N],b[N],cache[102][N],w;

int dp(int pos,int weight)
{
    if(weight>w)
        return -1e15;
    if(pos==n+1)
        return 0;
    int &ans=cache[pos][weight];
    if(ans!=-1)
        return ans;
    ans=max(b[pos]+dp(pos+1,weight+a[pos]),dp(pos+1,weight));
    return ans;
}

int32_t main()
{
    IOS;

    memset(cache,-1,sizeof cache);
    cin>>n>>w;

    for(int i=1;i<=n;i++)
        cin>>a[i]>>b[i];

    cout<<dp(1,0);

    return 0;
}