#include <bits/stdc++.h>
#define FIO ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
using namespace std;
const long double pi = 3.14159265358979323;
const double EPS = 1e-12;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;

std::vector<ll> v[27];
map<ll, ll> use;
int main(){
    FIO;
    ll n, q;
    cin >> n;
    string s;
    cin >> s;
    for(int i = 0; i < n; i++) v[s[i] - 'a'].push_back(i + 1);
    cin >> q;
    while(q--){
        ll b, k, flag = 0, pt = 0;
        cin >> s >> b >> k;
        ll tot = (n + b - 1) / b;
        use.clear();
        for(auto i : s){
            ll pos = upper_bound(v[i - 'a'].begin(), v[i - 'a'].end(), pt) - v[i - 'a'].begin();
            //cout << pos << " ";
            if(pos == (int)v[i - 'a'].size()){
                flag = -1;
                break;
            }
            else{
                pos = v[i - 'a'][pos];
                ll seg = (pos + b - 1) / b;
                use[seg]++;
                pt = pos;
                if(use[seg] == k){
                    pt = min(n, seg * b);
                }
            }
        }
        if(flag) cout << "No\n";
        else cout << "Yes\n";
    }

    return 0;
}