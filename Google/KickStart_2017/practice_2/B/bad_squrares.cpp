#include<bits/stdc++.h>

#define ssync ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
#define F first
#define S second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
typedef vector<ll> vll;
typedef vector<vll> vvl;
typedef pair<int,int> pii;
typedef pair<int,ll> pil;
typedef pair<ll,ll> pll;
const ll MOD = 1e9+7;
const ld PI = 3.14159265;

ll powerWithMod(ll base, ll exponent, ll modulus = LLONG_MAX)
{
    ll result = 1;
    base %= modulus;
    while(exponent > 0)
    {
        if(exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent >>= 1;
        base = (base * base) % modulus;
    }
    return result;
}

ll modInverse(ll a, ll m = MOD)
{
    return powerWithMod(a, m-2, m);
}

int t, r, c, k, x, y, a[3005][3005], dp[3005][3005];
ll ans;

int main()
{
    ssync;
    cin >> t;
    for(int cas=1; cas<=t; cas++)
    {
        cin >> r >> c >> k;
        ans=0;
        memset(a, 0, sizeof(a));
        memset(dp, 0, sizeof(dp));
        while(k--)
        {
            cin >> x >> y;
            a[++x][++y]=1;
        }
        for(int i=1; i<=r; i++)
        {
            for(int j=1; j<=c; j++)
            {
                if(a[i][j]==0)
                {
                    dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1;
                    ans += dp[i][j];
                }
            }
        }
        cout << "Case #" << cas << ": " << ans << "\n";
    }
    return 0;
}