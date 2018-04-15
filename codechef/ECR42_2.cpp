

#include <cstdio>


int n,c[2];
char s[200005];

int main()
{
    printf("%d %d\n",c[0],c[1]);
	scanf("%d %d %d",&n,c,c+1);
	scanf("%s",s+1);
	int ans=0;
	for (int i=1; i<=n; i++)
		if (s[i]=='.')
		{
			int j=i,k=(c[0]>=c[1]?0:1);
			while (j<=n&&s[j]=='.')
			{
				if (c[k]>0)
					ans++;
				c[k]--;
				k^=1;
				j++;
			}
			i=j;
		}
	printf("%d\n",ans);
	return 0;
}
/*
toggle=[1,1]
n, a, b = [int(x) for x in input().split()]
seats = input()
ans = 0
for i, v in enumerate(seats):
    if v == ".":
        j=i
        k=[1, 0][toggle[0]>=toggle[1]]
        while j < n and seats[j]==".":
            if toggle[k]>0:
                ans += 1
            toggle[k]-=1
            k^=1
            j+= 1
    i=j
print(ans)

*/


