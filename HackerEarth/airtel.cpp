Problem A:

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cctype>
#include <map>

using namespace std;

typedef long long LL;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

int n,odd,even;
map<int,int> bin;
LL ans;

int main()
{
    //freopen("subarrays.in","r",stdin),freopen("subarrays.out","w",stdout);
    n=read(),bin[0]=1,ans=0;
    for (int i=1,x;i<=n;++i) x=read(),odd+=x&1,even+=(x&1)^1,ans+=bin[odd-even],++bin[odd-even];

}

Problem B:

#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cctype>
#include <queue>

using namespace std;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

int buf[30];

inline void write(int x)
{
	if (x<0) putchar('-'),x=-x;
	for (;x;x/=10) buf[++buf[0]]=x%10;
	if (!buf[0]) buf[++buf[0]]=0;
	for (;buf[0];putchar('0'+buf[buf[0]--]));
}

const int N=1005;
const int D=4;

typedef pair<int,int> P;
#define mkp(a,b) make_pair(a,b)
#define ft first
#define sd second

int dir[D][2]={{1,0},{-1,0},{0,1},{0,-1}};
char MAP[N][N];
int dis[N][N];
int n,m,T,srcx,srcy;

queue<P> q;

void bfs()
{
	memset(dis,-1,sizeof dis);
	if (MAP[srcx][srcy]=='*') return;
	for (dis[srcx][srcy]=0,q.push(mkp(srcx,srcy));!q.empty();)
	{
		P data=q.front();q.pop();
		int curx=data.ft,cury=data.sd;
		for (int d=0,tarx,tary;d<D;++d)
		{
			tarx=curx+dir[d][0],tary=cury+dir[d][1];
			if (0<=tarx&&tarx<n&&0<=tary&&tary<m&&MAP[tarx][tary]!='*'&&!~dis[tarx][tary]) dis[tarx][tary]=dis[curx][cury]+1,q.push(mkp(tarx,tary));
		}
	}
}

int main()
{
	//freopen("grid.in","r",stdin),freopen("grid.out","w",stdout);
	n=read(),m=read(),T=read();
	for (int i=0;i<n;++i) scanf("%s",MAP[i]);
	srcx=read()-1,srcy=read()-1,bfs();
	for (int x,y;T--;) x=read()-1,y=read()-1,write(dis[x][y]),putchar('\n');
	//fclose(stdin),fclose(stdout);
	return 0;
}

Problem C:

#include <iostream>
#include <cstdio>
#include <cctype>

using namespace std;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

int buf[30];

inline void write(int x)
{
	if (x<0) putchar('-'),x=-x;
	for (;x;x/=10) buf[++buf[0]]=x%10;
	if (!buf[0]) buf[++buf[0]]=0;
	for (;buf[0];putchar('0'+buf[buf[0]--]));
}

const int N=100005;
const int E=N<<1;

int a[N],last[N],vis[N];
int tov[E],nxt[E];
int n,K,tot,ans,tar,ret,idx;

inline void insert(int x,int y){tov[++tot]=y,nxt[tot]=last[x],last[x]=tot;}

void dfs(int x,int cur=0)
{
	vis[x]=idx;
	if (cur>ret) ret=cur,tar=x;
	for (int i=last[x],y;i;i=nxt[i])
		if (vis[y=tov[i]]!=idx&&!(a[y]%K)) dfs(y,cur+1);
}

int main()
{
	//freopen("path.in","r",stdin),freopen("path.out","w",stdout);
	n=read(),K=read();
	for (int i=1;i<=n;++i) a[i]=read();
	for (int i=1,x,y;i<n;++i) x=read(),y=read(),insert(x,y),insert(y,x);
	for (int x=1;x<=n;++x)
		if (!vis[x]&&!(a[x]%K))
		{
			ret=tar=-1,++idx,dfs(x);
			int src=tar;ret=tar=-1,++idx,dfs(src);
			ans=max(ans,ret);
		}
	printf("%d\n",ans);
	//fclose(stdin),fclose(stdout);
	return 0;
}

Problem D:

#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cctype>

using namespace std;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

int buf[30];

inline void write(int x)
{
	if (x<0) putchar('-'),x=-x;
	for (;x;x/=10) buf[++buf[0]]=x%10;
	if (!buf[0]) buf[++buf[0]]=0;
	for (;buf[0];putchar('0'+buf[buf[0]--]));
}

const int P=1000000007;
const int N=100005;

int a[N];
int T,n,ans;

int main()
{
	//freopen("remove.in","r",stdin),freopen("remove.out","w",stdout);
	for (T=read();T--;printf("%d\n",ans))
	{
		n=read();
		for (int i=1;i<=n;++i) a[i]=read();
		sort(a+1,a+1+n,greater<int>()),ans=0;
		for (int i=1,s=1;i<=n;s=1ll*s*(++i)%P) (ans+=1ll*a[i]*s%P)%=P;
	}
	//fclose(stdin),fclose(stdout);
	return 0;
}

Problem E:

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cctype>
#include <vector>
#include <cmath>

using namespace std;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

const int N=300005;
const int Q=300005;
const int V=100000;
const int lim=316;
const int pcnt=65;

typedef pair<int,int> P;
#define mkp(a,b) make_pair(a,b)
#define ft first
#define sd second

int mxf[V+5],f[V+5],pri[V+5],app[V+5],id[V+5];
int a[N],sigsum[N],zerosum[N],bel[N];
bool is_sqr[Q],is_cube[Q];
vector<P> factor[V+5];
vector<int> sprime;
int sum[N][pcnt];
int n,q,q_,block_size,block_cnt,lcur,rcur;
int ret[2];

struct query
{
	int l,r,id;

	inline query(int l_=0,int r_=0,int id_=0){l=l_,r=r_,id=id_;}

	inline bool operator<(query const q)const{return bel[l]^bel[q.l]?bel[l]<bel[q.l]:bel[l]&1?r<q.r:r>q.r;}
}qry[Q];

inline int iabs(int x){return x>0?x:-x;}

void pre()
{
	f[1]=1;
	for (int i=2;i<=V;++i)
	{
		if (!f[i]) pri[++pri[0]]=f[i]=i;
		for (int j=1;j<=pri[0];++j)
		{
			if (1ll*i*pri[j]>V) break;
			f[i*pri[j]]=pri[j];
			if (!(i%pri[j])) break;
		}
	}
	for (int i=1;i<=pri[0]&&pri[i]<=lim;++i) sprime.push_back(pri[i]),id[pri[i]]=(int)sprime.size()-1;
	for (int x=1;x<=V;++x)
	{
		for (int v=x,y,cnt;v>1;factor[x].push_back(mkp(y,cnt)))
			for (y=f[v],cnt=0;!(v%y);v/=y,++cnt);
		mxf[x]=factor[x].empty()||factor[x].back().ft<=lim?0:factor[x].back().ft;
	}
	for (int i=1;i<=n;++i) sigsum[i]=sigsum[i-1]+(a[i]<0);
	for (int i=1;i<=n;++i) zerosum[i]=zerosum[i-1]+!a[i];
	for (int i=1;i<=n;++i)
	{
		for (int j=0;j<pcnt;++j) sum[i][j]=sum[i-1][j];
		for (auto p:factor[iabs(a[i])]) if (p.ft<=lim) sum[i][id[p.ft]]+=p.sd;
	}
}

inline void add(int x)
{
	int p;
	if (!(p=mxf[iabs(a[x])])) return;
	if (app[p]&1) --ret[0];
	else ++ret[0];
	if (app[p]%3==2) --ret[1];
	else if (!(app[p]%3)) ++ret[1];
	++app[p];
}

inline void del(int x)
{
	int p;
	if (!(p=mxf[iabs(a[x])])) return;
	if (app[p]&1) --ret[0];
	else ++ret[0];
	if (app[p]%3==1) --ret[1];
	else if (!(app[p]%3)) ++ret[1];
	--app[p];
}

void solve()
{
	if (!q_) return;
	block_size=max(1,(int)trunc(sqrt(1.*n/q_))),block_cnt=0;
	for (int cur=1,tar;cur<=n;cur=tar)
	{
		tar=min(n+1,cur+block_size),++block_cnt;
		for (int i=cur;i<tar;++i) bel[i]=block_cnt;
	}
	sort(qry+1,qry+1+q_),lcur=1,rcur=0;
	for (int i=1;i<=q_;++i)
	{
		for (;rcur<qry[i].r;add(++rcur));
		for (;rcur>qry[i].r;del(rcur--));
		for (;lcur<qry[i].l;del(lcur++));
		for (;lcur>qry[i].l;add(--lcur));
		is_sqr[qry[i].id]&=!ret[0],is_cube[qry[i].id]&=!ret[1];
	}
}

int main()
{
	//freopen("sqrcube.in","r",stdin),freopen("sqrcube.out","w",stdout);
	n=read(),q=read();
	for (int i=1;i<=n;++i) a[i]=read();
	pre();
	for (int i=1,l,r;i<=q;++i)
	{
		is_sqr[i]=is_cube[i]=1,l=read(),r=read();
		if (!(zerosum[r]-zerosum[l-1]))
		{
			if ((sigsum[r]^sigsum[l-1])&1) is_sqr[i]=0;
			for (auto x:sprime) is_sqr[i]&=!((sum[r][id[x]]-sum[l-1][id[x]])&1),is_cube[i]&=!((sum[r][id[x]]-sum[l-1][id[x]])%3);
			if (is_sqr[i]||is_cube[i]) qry[++q_]=query(l,r,i);
		}
	}
	solve();
	for (int i=1;i<=q;++i)
		if (is_sqr[i]&&is_cube[i]) printf("Both\n");
		else if (is_sqr[i]) printf("Square\n");
		else if (is_cube[i]) printf("Cube\n");
		else printf("None\n");
	//fclose(stdin),fclose(stdout);
	return 0;
}

Problem F:

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

inline int read()
{
	int x=0,f=1;
	char ch=getchar();
	while (!isdigit(ch)) f=ch=='-'?-1:f,ch=getchar();
	while (isdigit(ch)) x=x*10+ch-'0',ch=getchar();
	return x*f;
}

const int N=100005;
const int E=N<<1;
const int V=1000000;
const int MAXK=10;

map<int,int> f[N][MAXK];
int last[N],a[N],fmx[N];
int fp[V+5],pri[V+5];
vector<int> pd[V+5];
int tov[E],nxt[E];
int n,tot,K,ans;

inline void insert(int x,int y){tov[++tot]=y,nxt[tot]=last[x],last[x]=tot;}

int gcd(int x,int y){return y?gcd(y,x%y):x;}

void pre()
{
	fp[1]=1;
	for (int i=2;i<=V;++i)
	{
		if (!fp[i]) pri[++pri[0]]=fp[i]=i;
		for (int j=1;j<=pri[0];++j)
		{
			if (1ll*i*pri[j]>V) break;
			fp[i*pri[j]]=pri[j];
			if (!(i%pri[j])) break;
		}
	}
	for (int x=1;x<=V;++x)
		for (int v=x,y;v>1;pd[x].push_back(y))
			for (y=fp[v];!(v%y);v/=y);
}

void dp(int x,int fa=0)
{
	for (int p:pd[a[x]]) f[x][1][p]=1;
	map<int,int> f_[MAXK]=f[x];
	vector<int> son;
	for (int i=last[x],y,g;i;i=nxt[i])
		if ((y=tov[i])!=fa)
		{
			son.push_back(y),dp(y,x),g=gcd(a[x],a[y]);
			for (int p:pd[g])
				for (int j=1;j<K;++j)
					if (f[x][j].find(p)!=f[x][j].end()&&f[y][K-j].find(p)!=f[y][K-j].end())
						ans=max(ans,f[x][j][p]+f[y][K-j][p]);
			for (int p:pd[a[x]])
			{
				f[x][1][p]=max(f[x][1][p],fmx[y]+1);
				if (f[x][0].find(p)!=f[x][0].end()) ans=max(ans,f[x][0][p]+fmx[y]);
			}
			for (int p:pd[g])
				for (int j=1;j<K;++j)
					if (f[y][j].find(p)!=f[y][j].end())
						f[x][(j+1)%K][p]=max(f[x][(j+1)%K][p],f[y][j][p]+1);
		}
	reverse(son.begin(),son.end());
	for (int y:son)
	{
		int g=gcd(a[x],a[y]);
		for (int p:pd[g])
			for (int j=1;j<K;++j)
				if (f_[j].find(p)!=f_[j].end()&&f[y][K-j].find(p)!=f[y][K-j].end())
					ans=max(ans,f_[j][p]+f[y][K-j][p]);
		for (int p:pd[a[x]])
		{
			f_[1][p]=max(f_[1][p],fmx[y]+1);
			if (f_[0].find(p)!=f_[0].end()) ans=max(ans,f_[0][p]+fmx[y]);
		}
		for (int p:pd[g])
			for (int j=1;j<K;++j)
				if (f[y][j].find(p)!=f[y][j].end())
					f_[(j+1)%K][p]=max(f_[(j+1)%K][p],f[y][j][p]+1);
	}
	for (int p:pd[a[x]]) fmx[x]=max(fmx[x],f[x][0][p]);
}

int ret,tar,idx;
int vis[N];

void dfs(int x,int cur=1)
{
	vis[x]=idx;
	if (cur>ret) ret=cur,tar=x;
	for (int i=last[x],y;i;i=nxt[i])
		if (vis[y=tov[i]]!=idx&&a[y]!=1) dfs(y,cur+1);
}

int main()
{
	//freopen("gcd.in","r",stdin),freopen("gcd.out","w",stdout);
	n=read(),K=read(),pre();
	for (int i=1,x,y;i<n;++i) x=read(),y=read(),insert(x,y),insert(y,x);
	for (int i=1;i<=n;++i) a[i]=read();
	if (K!=1) dp(1);
	else
	{
		for (int x=1;x<=n;++x)
			if (!vis[x])
			{
				ret=tar=-1,++idx,dfs(x);
				int src=tar;ret=tar=-1,++idx,dfs(src);
				ans=max(ans,ret);
			}
	}
	printf("%d\n",ans);
	//fclose(stdin),fclose(stdout);
	return 0;
}