#include "bits/stdc++.h"
using namespace std;
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")
#pragma GCC optimize("Ofast,no-stack-protector")
#pragma GCC target("avx,tune=native")
#pragma GCC optimize ("unroll-loops")
const int maxn = 100100;
long long sum[maxn], val[maxn], w[maxn];
int in[maxn], out[maxn], where[maxn], res[maxn], T = 1;
vector<pair<int, int> > g[maxn], q[maxn];
void init(int cur, int p = -1){
	val[T] = sum[cur] + w[cur];
	in[cur] = T++;
	for(auto e : g[cur]){
		if(e.first == p) continue;
		sum[e.first] = sum[cur] + e.second;
		init(e.first, cur);
	}
	out[cur] = T;
	q[out[cur]-1].push_back({in[cur], cur});
}
int bit[maxn];
void add(int p, int x){
	for(; p < maxn; p += p & - p) bit[p] += x;
}
int que(int p){
	int ans = 0;
	for(; p; p -= p & - p) ans += bit[p];
	return ans;
}
int main(){
	int n;
	scanf("%d", &n);
	for(int e = 0; e < n - 1; e++){
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		g[u].push_back({v, w});
		g[v].push_back({u, w});
	}
	for(int e = 1; e <= n; e++) scanf("%lld", w + e);
	init(1);
	map<long long, int> lst;
	for(int e = 1; e < T; e++){
		auto it = lst.find(val[e]);
		if(it != lst.end()) add(it->second, -1);
		add(e, 1);
		lst[val[e]] = e;
		for(auto f : q[e])
			res[f.second] = que(e) - que(f.first-1);
	}
	for(int e = 1; e <= n; e++)
		printf("%d\n", res[e]);
    return 0;
}