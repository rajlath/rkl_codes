#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
const ll mod=1000000007;
ll powmod(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b) { return b?gcd(b,a%b):a;}
// head

int n,f[50],sz[50];
char g[50][50];
int find(int x) { return f[x]==x?x:f[x]=find(f[x]); }
int cc[50],p[50],tot,id[50],G[50][50];
int main() {
	scanf("%d",&n);
	rep(i,0,n) f[i]=i;
	rep(i,0,n) {
		scanf("%s",g[i]);
		rep(j,0,n) if (g[i][j]=='A') f[find(i)]=find(j);
	}
	rep(i,0,n) rep(j,0,n) if (g[i][j]=='X'&&find(i)==find(j)) {
		puts("-1");
		return 0;
	}
	rep(i,0,n) sz[find(i)]++;
	int ret=n-1;
	rep(i,0,n) if (find(i)==i&&sz[i]!=1) id[i]=tot++;
	rep(i,0,n) rep(j,0,n) if (g[i][j]=='X'&&sz[find(i)]!=1&&sz[find(j)]!=1) {
		G[id[find(i)]][id[find(j)]]=1;
	}
	rep(i,0,tot) p[i]=i;
	int mcol=tot;
	while (clock()<=4.9*CLOCKS_PER_SEC) {
		random_shuffle(p,p+tot);
		int col=1;
		rep(i,1,tot) {
			int S=0;
			rep(j,0,i) if (G[p[j]][p[i]]) S|=(1<<cc[j]);
			S^=(1<<col)-1;
			if (S==0) cc[i]=col,col++;
			else {
				while (1) {
					cc[i]=rand()%(col+1);
					if (S&(1<<cc[i])) {
						break;
					}
				}
			}
		}
		mcol=min(mcol,col);
	}
	printf("%d\n",ret+mcol);
}