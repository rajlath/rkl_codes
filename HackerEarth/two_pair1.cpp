using namespace std;
#include<bits/stdc++.h>
#define foreach(it, x) for(typeof (x).begin() it = (x).begin(); it != (x).end(); ++it)
#define ___ ios_base::sync_with_stdio(false);cin.tie(NULL);
#define D(x) cout<<#x " = "<<(x)<<endl


typedef long long ll;

vector<int> factors(const int &n){
    vector<int> ans;
    int sn = sqrt(n);
    for(int i = 1; i <= sn; ++i){
        if(n%i == 0) {
            ans.push_back(i);
            ans.push_back(n/i);
        }
    }

    sort(ans.begin(), ans.end());
    ans.resize(distance(ans.begin(),unique(ans.begin(), ans.end())));
    return ans;
}

int k ;
const ll mod = 1e9 + 7;

ll mod_pow(ll a, int b){
    ll ans = 1;
    while(b){
        if(b&1) ans = (ans*a) % mod;
        a = (a * a) % mod;
        b>>=1;
    }
    return ans;
}
map<int, ll> _dp;

ll dp(int n){
    if(_dp.count(n) != 0) return _dp[n];

    if(n==1) return _dp[n] = k;
    vector<int> fac = factors(n);
    ll ans = 0;
    for(int i = 0; i < fac.size() - 1; ++i)
        ans = (ans + dp(fac[i]))%mod;
    ans = mod - ans;
    ll p = mod_pow(k,n);
    return _dp[n] = (p + ans)%mod;
}

int main()
{
     int n, _k;
     cin >> n >> _k;
     k = _k;
      _dp.clear();
     vector<int> fac = factors(n);
     ll ans = 0;
     for(int i = 0; i < fac.size(); ++i){
            ans = (ans + ((dp(fac[i]) * (ll)fac[i]) % mod )) % mod;
        }
    cout<<ans;



}


