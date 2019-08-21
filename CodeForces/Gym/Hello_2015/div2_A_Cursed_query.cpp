#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define rof(i,a,b) for(int (i)=(a);(i) > (b); --(i))
#define rep(i, c)	for(auto &(i) : (c))
#define x     first
#define y     second
#define pb  push_back
#define PB  pop_back()
#define iOS  ios_base::sync_with_stdio
#define mp(a,b) make_pair(a,b)
#define sqr(a)  ((1LL * (a) * (a)))
#define all(a)  a.begin() , a.end()
#define error(x) cerr << #x << " = " << (x) <<endl
#define Error(a,b) cerr<<"( "<<#a<<" , "<<#b<<" ) = ( "<<(a)<<" , "<<(b)<<" )\n";
#define errop(a) cerr<<#a<<" = ( "<<((a).x)<<" , "<<((a).y)<<" )\n";
#define coud(a,b) cout<<fixed << setprecision((b)) << (a)
#define double long double
typedef pair<int,int> pii;
typedef tree<pii, null_type, less<pii>, rb_tree_tag, tree_order_statistics_node_update>	os;
typedef long long ll;
const int maxn = 1e5 + 100;
int a[maxn],n,q;
ll s[maxn], t, sum;
int main(int argc,char ** argv){
    iOS(false);
    cin >> n >> q;
    For(i,0,n)
        cin >> a[i], sum += 1LL * a[i], s[i] = sum;
    while(q--){
        cin >> t;
        t %= s[n-1];
        cout << 1 + (lower_bound(s,s+n,t+1LL) - s) << endl;
    }
}