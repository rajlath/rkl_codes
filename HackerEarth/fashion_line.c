#include <stdio.h>
char str[10005], special[63];
int isspecial(char c, int k)
{   int i;
	for (i=0; i<k; i++)
		if (c==special[i]) return 1;
	return 0;
}
int main()
{
	int t;
	scanf ("%d", &t);
	while (t--)
	{
		int n, k, lneed, rneed,i;
		scanf ("%d %d %d %d ", &n, &k, &lneed, &rneed);
		scanf ("%s %s", &str, &special);
		for (i=0; i<n; i++)
			if (isspecial(str[i], k))
				str[i]='-';
		int ans=0, l=-1, r=-1, lcnt=0, rcnt=0;
		for (i=0; i<n; i++)
		{
			while (l<n && lcnt<lneed)
			{
				l++;
				if (str[l]=='-') lcnt++;
			}
			while (r<n-1 && rcnt<=rneed)
			{
				r++;
				if (str[r]=='-') rcnt++;
			}
			if (str[r]=='-' && rcnt>rneed)
			{
				r--;
				rcnt--;
			}
			if (lneed==0) ans+=r-i+1;
			else ans+=r-l+1;
			if (str[i]=='-')
			{
				lcnt--;
				rcnt--;
			}
		}
		printf ("%d\n", ans);
	}
    return 0;
}

