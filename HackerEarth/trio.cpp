#include <bits/stdc++.h>
using namespace std;
 
#define fast ios_base::sync_with_stdio(false);cin.tie(0)
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define snd sd.ft
#define td sd.sd
#define debug(x) cout<<"### x is: "<<x<<"###"<<endl
#define all(a) a.begin(),a.end()
#define tc int t;scanf("%d",&t);while (t-->0)
 
#define ninf -1000000000
#define pinf 1000000000
 
typedef long long ll;
const ll MOD= 1e9+7;
typedef vector<pair<ll,ll> > vecpair;
typedef vector<pair<ll, pair<ll,ll> > > vecpair3;
 
ll power(ll a, ll b) {ll ret=1;while(b) {if(b&1) ret*=a;a*=a;if(ret>=MOD) ret%=MOD;if(a>=MOD) a%=MOD;b>>=1;}return ret;}
ll invmod(ll x) {return power(x,MOD-2);}
 
ll mpp[100005];
vector<ll> v;
 
int main()
{
 
    //freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	int n,i,j,m;
 
	scanf("%d %d",&n,&m);
	
	ll a[n+1];
	
	for(i=1;i<=n;i++)
	scanf("%lld",a+i) , mpp[a[i]%m]++;
	printf("%lld", mpp[m]);
	ll ans =0,md=0;
	
	for(i=0;i<m;i++)
	{
		for(j=i+1;j<=m;j++)
		{
			md= (m - (i+j)%m)%m;
			
			if(md > i && md > j)
			ans += (mpp[i] * mpp[j] * mpp[md]);
		}
		
		md = (m- (2*i)%m)%m;
		
		if(md != i && i !=0)
		ans += ((mpp[i] * (mpp[i]-1))/2  * mpp[md]);
		else
		ans += (mpp[i] * (mpp[i]-1) * (mpp[i]-2))/6;
	}
	
	printf("%lld",ans);
	
	return 0;
}
