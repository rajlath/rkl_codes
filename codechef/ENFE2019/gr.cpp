#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long

const int N=1e5+5;

int n, m;
int ans=1;
int vis[N], col[N];
vector<int> g[N];

void dfs(int u, int c)
{
    if(vis[u])
    {
        if(col[u]!=c)
            ans=0;
        return;
    }
    vis[u]=1;
    col[u]=c;
    for(auto &it:g[u])
        dfs(it, c^1);
}

int32_t main()
{
    IOS;
    int t;
    cin>>t;
    while(t--)
    {
        ans=1;
        cin>>n>>m;
        for(int i=1;i<=n;i++)
        {
            vis[i]=0;
            g[i].clear();
        }
        for(int i=1;i<=m;i++)
        {
            int u, v;
            cin>>u>>v;
            g[u].push_back(v);
            g[v].push_back(u);
        }
        for(int i=1;i<=n;i++)
        {
            if(!vis[i])
                dfs(i, 0);
        }
        if(ans)
            cout<<"YeS"<<endl;
        else
            cout<<"No"<<endl;
    }
    return 0;
}
