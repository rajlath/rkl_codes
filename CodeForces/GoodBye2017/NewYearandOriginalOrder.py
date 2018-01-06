#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MM = 1e9 + 7;
const int MAXN = 2222 + 10;

int n;
ll cnt[MAXN];
char s[MAXN];
ll pw(ll p,ll q){if(!q)return 1; ll r=1; for(;q;q>>=1){if(q&1)r=r*p%MM;p=p*p%MM;}return r;}
ll gao(ll x,ll c,ll d,ll m){return (((pw(10,c)*pw(100-9*x,m)-pw(91-9*x,m))%MM*x%MM*pw(9,MM-2)%MM)+MM)%MM;}

int main(){
	scanf("%s", s + 1);
	n = strlen(s + 1);
	ll ans = 0;
	for (int i = 1; i <= n; i++){
		for (int j = 0; j < 10; j++) cnt[j] = 0;
		for (int j = 1; j < i; j++) cnt[s[j] - '0']++;
		for (int k = 0; k < s[i] - '0' + (i == n); k++){
			cnt[k]++;
			int nn = n - i, les = 0;
			for (int j = 0; j < 10; j++){
				ans = (ans + gao(j, cnt[j], les, nn) * pw(10, i - les - cnt[j])) % MM;
				les += cnt[j];
			}
			cnt[k]--;
		}
	}
	printf("%lld\n", (ans % MM + MM) % MM);
	return 0;
}
→Judgement Protocol


#include<bits/stdc++.h>
#define ALL(c) (c).begin(), (c).end()
using namespace std;
using ll = long long;
using ld = long double;

const int N = 1e6+6;
const int mod = 1e9+7;


ll brute(int n){
	ll res;
	for(int x=1;x<=n;++x){
		string s = to_string(x);
		sort(ALL(s));
		for(char &c : s) if(c!='7') c = '0';
		res+=stoi(s);
	}
	return res;
}

ll gg(string s, int c){
	int n = s.size();
	vector<ll> f(n+1), g(n+1);

	f[0] = 0;
	g[0] = 1;

	for(int k=1;k<=n;++k){
		for(int x=0;x<10;++x){
			if(x<c){
				f[k]+=f[k-1];
				g[k]+=g[k-1];
			}else
			if(x>c){
				f[k]+=f[k-1]*10;
				g[k]+=g[k-1]*10;
			}else{
				f[k]+=f[k-1]*10+g[k-1];
				g[k]+=g[k-1];
			}
			f[k]%=mod;
			g[k]%=mod;
		}
	}

	ll ans = 0;
	for(int i=0;i<n;++i){
		ll F = f[n-i-1], G = g[n-i-1];
		for(int j=0;j<i;++j){
			int x = s[j]-'0';
			if(x>c){
				F = F*10 %mod;
				G = G*10 %mod;
			}else
			if(x==c){
				F = (F*10 + G) %mod;
			}
		}

		for(int x=0;x<s[i]-'0';++x){
			if(x>c){
				ans+=F*10%mod;
			}else
			if(x<c){
				ans+=F;
			}else{
				ans+=(F*10+G)%mod;
			}
			ans%=mod;
		}
	}

	sort(ALL(s));

	ll ten = 1;
	for(int i=0;i<n;++i){
		int x = s[n-i-1]-'0';
		if(x==c){
			ans+=ten;
			ans%=mod;
		}
		ten = ten*10%mod;
	}

	return ans;
}


int main(){
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);cin.tie(0);//cout.precision(12);cout<<fixed;



	string s;
	cin>>s;

	ll ans = 0;
	for(int c=1;c<10;++c){
		ll val = gg(s, c);
		cerr<<c<<": "<<val<<endl;
		ans+=val*c;
		ans%=mod;
	}

	cout<<ans<<endl;


	return 0;
}