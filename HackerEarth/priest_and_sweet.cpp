/******************************************
*    AUTHOR         :   VIVEK SHAH        *
*    INSTITUTION    :   NIT SURAT         *
******************************************/
 
#include <bits/stdc++.h>
 
#define boost ios_base::sync_with_stdio(false);cin.tie(NULL)
#define ll long long int
#define mod 1000000007
#define what_is(x) cout << #x << " is " << x << endl;
#define llt ll test;cin>>test;while(test--)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(v) v.begin(),v.end()
#define allr(v) v.rbegin(),v.rend()
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define len(s) s.length()
#define MAX 1000000000
 
using namespace std;
 
std::map<ll, ll> m;
ll n;
 
ll power(ll a, ll b){
    
	ll res = 1;
	while(b){
		if(b%2==1){
			res = (res*a)%mod;
		}
		a = (a*a)%mod;
		b/=2;
	}
	if(n%2==0)res-=1;
	else res = (res+1)%mod;
	return res;
}
 
 
int main()
{
	boost;
		
	m[0] = 0;
	m[1] = 1;
	m[2] = 1;
 
	llt{
		cin>>n;
		if(n==1 || n==2)cout<<"1\n";
		else{
 			if(m[n]!=0){cout<<m[n]<<"\n";continue;}
			ll ans = (power(2,n) * 333333336)%mod;
 			m[n] = ans;
			cout<<ans%mod<<"\n";
		}
	}
 
	return 0;
}
