#copied
From the question, it is clear that the person nearest to Rick has maximum chances of killing him.
Thus sort the array.
Case 1 : No time for Reload 
Now if reload doesn't take any time then 
for( i=0; i< size; i++ ) 
if( arr[i] - i > 0 ) count++; 
else break;
thus count would have given the solution because for first person in array he is at same distance as before, 2nd person has gone 1 step closer , 3rd person 2 steps closer..
thus ith person would have come (i-1) steps closer if the reload doesn't take time
Case 2 : Consider reload time 
It can be included in case 1 simply by taking another variable sub initialized to 0. 
so that c=0, sub=0
for( i=0; i< size; i++ ) {
if( arr[i] - i - sub> 0 ) count++; 
else break;
c=c+1;
if( c==6) sub++,c=0; // Reload 
}
Thus count is the solution because number of times it is reloaded others killers would have come closer by that amount and thus needs to be further subtracted.
NOTE: condition is > 0 and not >= 0 because equal means it has reached Rick and thus killed him
#include<bits/stdc++.h>
using namespace std;
int ar[50005];
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		memset(ar,0,sizeof(ar));
		int n,tmp;
		scanf("%d",&n);
		for(int i=1;i<=n;++i)
		{
			scanf("%d",&tmp);
			ar[tmp]++;
		}
		int ans=0,cnt=0,j=0;
		bool pos=true;
		for(int i=1;i<=n;++i)
		{
			while(ar[j]==0)
				j++;
			ar[j]--;
			if(j-cnt<=0)
			{
				pos=false;
				break;
			}
			if(i%6==0 && i!=0)
				cnt++;
			cnt++;
			ans++;
		}
		if(pos)
			printf("Rick now go and save Carl and Judas\n");
		else
			printf("Goodbye Rick\n%d\n",ans);
	}
	return 0;
