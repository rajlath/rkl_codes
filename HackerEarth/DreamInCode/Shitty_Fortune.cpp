#include <bits/stdc++.h>
using namespace std;
#define ll long long int
const int N = 500005;
ll BIT[N][52];
void update(int idx, int x, ll val) {
	while(idx<N){
		BIT[idx][x] += val;
		idx += idx&-idx;
	}
}
ll query(int idx, int x){
	ll ret = 0;
	while(idx){
		ret += BIT[idx][x];
		idx -= idx&-idx;
	}
	return ret;
}
int main()
{
	int n;
	cin>>n;
	int a[n+9];
	for(int i=1;i<=n;i++)
		cin>>a[i];
	update(1,0,1);
	for(int i=n;i>=1;i--){
		for(int j = 1; j <= 4; j++)
			update(a[i]+2, j, query(a[i]+1, j-1));
	}
	cout<<query(N-1,4)<<endl;
}