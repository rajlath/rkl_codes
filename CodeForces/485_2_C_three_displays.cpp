int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin>>n;
	ll ar[n],br[n];
	for(int i=0;i<n;i++)
	{
		cin>>ar[i];
	}
	for(int i=0;i<n;i++)
	{
		cin>>br[i];
	}
	ll res=M;
	for(int i=1;i<n-1;i++)
	{
		ll mn1=M,mn2=M;
		for(int j=i-1;j>=0;j--)
		{
			if(ar[j]<ar[i])
			{
				mn1=min(br[j],mn1);
			}
		}
		if(mn1==M)
			continue;
		for(int j=i+1;j<n;j++)
		{
			if(ar[j]>ar[i])
			{
				mn2=min(br[j],mn2);
			}
		}
		if(mn1==M)
			continue;
		res=min(res,(mn1+mn2+br[i]));
	}
	if(res==M)
	{
		cout<<-1;
	}
	else
	{
		cout<<res;
	}
	return 0;
}