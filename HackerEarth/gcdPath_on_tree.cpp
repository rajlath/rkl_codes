// GCD Path on a Tree

#include <bits/stdc++.h>
using namespace std;

int K;

int A[100005], parent[100005][10], G[100005][10];
int dp[100005], dpMax[100005];

map<int, int> M;
vector<int> X[100005], Y[100005], prime[1000006], child[100005][10];
vector< map<int, int> > memo[100005];

void dfs(int i, int par)
{
parent[i][0] = i, parent[i][1] = par;
G[i][0] = A[i], G[i][1] = __gcd(A[par], A[i]);

for(int j=2; j<K; j++)
{
parent[i][j] = parent[par][j-1];
G[i][j] = __gcd(G[par][j-1], A[i]);
}

for(int j=0; j<K; j++)
if(parent[i][j])
child[ parent[i][j] ][j].push_back(i);

if(G[i][K-1] > 1 && parent[i][K-1] > 0)
Y[ parent[i][K-1] ].push_back(i);

for(int j=0; j<X[i].size(); j++)
if(X[i][j] != par)
dfs(X[i][j], i);
}

int solve(int i)
{
if(dp[i] != -1)
return dp[i];

int ans = 0;

for(int j=0; j<Y[i].size(); j++)
{
int node = Y[i][j];
ans = max(ans, 1);

for(int k=0; k<X[node].size(); k++)
if(X[node][k] != parent[node][1])
ans = max(ans, 1 + solve(X[node][k]));
}

return dp[i] = ans;
}

int getMask(int val)
{
int mask = 0;

for(int j=0; j<prime[val].size(); j++)
mask |= (1<<M[ prime[val][j] ]);

return mask;
}

int func(int i)
{
int val = A[i], k = 0;

for(int j=0; j<prime[val].size(); j++)
M[ prime[val][j] ] = k++;

int children = 0;

for(int j=0; j<X[i].size(); j++)
{
if(X[i][j] == parent[i][1])
continue;

memo[children].clear();
int node = X[i][j];

for(int k=0; k<K; k++)
{
map<int, int> childMap;

if(k == 0)
childMap[getMask(A[i])] = dp[node];
else
{
for(int x=0; x<child[node][k-1].size(); x++)
{
int ptr = child[node][k-1][x];
int mask = getMask(G[ptr][k]);

if(mask > 0)
childMap[mask] = max(childMap[mask], dpMax[ptr]);
}
}

memo[children].push_back(childMap);
}

children++;
}

int ans = dp[i];

for(int j=1; j<children; j++)
{
for(int k=0; k<K; k++)
{
int rem = K - 1 - k;

for(map<int, int>::iterator it1=memo[j-1][rem].begin(); it1!=memo[j-1][rem].end(); it1++)
for(map<int, int>::iterator it2=memo[j][k].begin(); it2!=memo[j][k].end(); it2++)
if(it1->first&it2->first)
ans = max(ans, it1->second + it2->second + 1);
}

for(int k=0; k<K; k++)
for(map<int, int>::iterator it=memo[j-1][k].begin(); it!=memo[j-1][k].end(); it++)
memo[j][k][it->first] = max(memo[j][k][it->first], it->second);

memo[j-1].clear();
}

M.clear();
return ans;
}

int main()
{
cin.tie(NULL), cout.tie(NULL);

int N;
cin >> N >> K;

for(int i=2; i<=1000000; i++)
if(prime[i].empty())
for(int j=i; j<=1000000; j+= i)
prime[j].push_back(i);

for(int i=1; i<=N-1; i++)
{
int u, v;
cin >> u >> v;

X[u].push_back(v);
X[v].push_back(u);
}

for(int i=1; i<=N; i++)
cin >> A[i];

dfs(1, 0);
memset(dp, -1, sizeof(dp));

for(int i=1; i<=N; i++)
dp[i] = solve(i);

for(int i=1; i<=N; i++)
for(int j=0; j<X[i].size(); j++)
if(X[i][j] != parent[i][1])
dpMax[i] = max(dpMax[i], dp[ X[i][j] ]);

int ans = 0;

for(int i=1; i<=N; i++)
ans = max(ans, func(i));

cout << ans * K << "\n";
return 0;
}