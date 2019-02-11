#include <bits/stdc++.h>

using namespace std;

#define PI acos(-1)
#define mod 1000000007
#define ll long long
#define nitro std::ios_base::sync_with_stdio (false); cin.tie(NULL)
#define pb push_back
#define mp make_pair
#define vi vector < int >
#define mod 1000000007
#define md 998244353
#define rep(i,a,b) for(int i=a;i<b;i++)
#define FF first
#define SS second
#define all(a) (a).begin(),(a).end()

int main () {
    nitro;

    #ifdef DBG
        freopen("in","r",stdin);
    #endif

    ll n; cin >> n;
    map<ll,string> m1;
    ll a = 1;
    ll low = 1;
    rep(i,0,27) {
        if(i%2 == 0) {
            string val(1,char(65 + i));
            m1[a] = val;
            if(i != 0){
                m1[a-low] = m1[low] + m1[a];
                low *= 10;
            }
            a *= 5;
        }
        else {
            string val(1,char(65+i));
            m1[a] = val;
            m1[a-low] = m1[low] + m1[a];
            a *= 2;
        }
    }

    string ans = "";
    while(n > 0){
        ll pre = 1;
        for(auto it : m1){
            if(it.FF > n) break;
            pre = it.FF;
        }
        int q = n/pre;
        cout<<q<<" "<<pre<<endl;
        n = n%pre;
        while(q--){
            ans+=m1[pre];
        }
    }
    cout << ans << endl;
    return 0;
}