#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long n,q,i,val,a[210000],count[50],tp,subs,ans;
	cin >> n >> q;
	for(i=1;i<=n;i++)
	{
		cin >> a[i];
		val= (long long)log2(a[i]);
		cout << val;
		count[val]++;
	}
	while(q--)
	{
		ans=0;
		cin >> val;
		i=33;
		while(val&&i>=0)
		{
			tp=count[i];
			subs=pow(2,i);
			if(count[i]>=val/subs)
			{
				ans+=val/subs;
				val=val%subs;
			}
			else
			{
				ans+=tp;
				val=val-tp*subs;
			}
			i--;
		}
		if(val==0)
		{
			cout << ans << endl;
		}
		else
			cout << "-1\n";
	}
	return 0;
}