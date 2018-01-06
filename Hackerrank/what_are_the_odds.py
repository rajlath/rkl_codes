'''
int main()
{
	// freopen("input.txt","r",stdin);
 	// freopen("output.txt","w",stdout);
	ll t=1;
	//s(t);
	while(t--){
		ll n;
		cin>>n;
		vector<ll>ar(n+2);
		for(ll i=1;i<=n;i++)cin>>ar[i];

		vector<ll>pref(n+2);
		pref[1]=ar[1];
		for(ll i=2;i<=n;i++)pref[i]=ar[i]^pref[i-1];

		unordered_map<ll,ll> cnt;

		ll suf=0;
		ll ans=0;
		cnt[0]=1;
		for(ll i=n;i>0;i--){
			ans+=cnt[pref[i-1]];
			suf^=ar[i];
			cnt[suf]++;
		}
		cout<<ans<<endl;

	}
}
'''
n = int(input())
piles = [int(x) for x in input().split()]
pref  = [0] * (n + 1)
pref[1] = piles[1]
for i in range(1, n):
    pref[i] = piles[i] ^ pref[i-1]
suf = 0
ans = 0
cnt = {}
cnt[0] = 1
for i in range(1, n):
    cnt[i] = 0
for i in range(n-1, -1, -1):
    ans += cnt[pref[i-1]]
    suf ^= piles[i-1]
    cnt[suf] += 1
print(ans)