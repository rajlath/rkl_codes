/*
Author: Arihant Gupta, IIIT Hyderabad, arihant_28
*/
#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> ii;
const int mod=1000000007;
const int DX[]={1,0,-1,0},DY[]={0,1,0,-1};
#define SSTR( x ) dynamic_cast< ostringstream & >( \
				( ostringstream() << dec << x ) ).str()
#define fill(a,b) memset(a,b,sizeof(a))
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define f first
#define s second
#define Pi 3.1415926535897
#define checkbit(n,b) ( (n >> b) & 1)
#define bsearch(arr,ind) (int)(lower_bound(all(arr),ind)-arr.begin())
#define LL long long int
#define eps 1e-9
#define all(x) (x).begin(),(x).end()
LL C(int n,int k){long long ans=1;k=k>n-k?n-k:k;int j=1;for(;j<=k;j++,n--){if(n%j==0){ans*=n/j;}else if(ans%j==0){ans=ans/j*n;}else{ ans=(ans*n)/j;}} return ans;}
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
LL gcd(LL a,LL b){if(a==0)return(b);else return(gcd(b%a,a));}
LL powmod(LL a,LL b,LL m) {LL res=1;a%=m;for(;b;b>>=1){if(b&1)res=res*a%m;a=a*a%m;}return res;}
LL maxi = 1000000000000000000;
int main()
{
	int t;
	scanf("%d",&t);;
	assert(t and t<=10e5);
	while(t--){
		LL n;
		scanf("%lld",&n);
		assert(n and n<=maxi);
		LL ans=0;
		LL cur=2;
		bool flag=true;
		int times=1;
		while(flag){
			int div=times;
			while(flag and div){
				LL t=cur+(cur>>div);
				if(t<=n){
					ans+=t;
					ans%=mod;
				}
				else{
					flag=false;
					break;
				}
				div--;
			}
			cur=cur<<1;
			times++;
		}
		printf("%lld\n",ans);
	}
	return 0;
}
