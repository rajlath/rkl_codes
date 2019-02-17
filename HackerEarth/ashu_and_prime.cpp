#include<bits/stdc++.h>
using namespace std;

int lp[1000001]={0};
int c[1000001]={0};
void lowestprime()
{
int i,j;
for(i=2;i<=1000000;i++)
{
if(lp[i]==0)
{
for(j=i;j<=1000000;j=j+i)
{
if(lp[j]==0)
lp[j]=i;
}
}

}
for(i=0;i<=1000000;i++)
c[lp[i]]++;
c[0]=c[1]=0;
}

int main()
{
lowestprime();
int t;
scanf("%d",&t);
while(t--)
{
int x;
scanf("%d",&x);
printf("%d\n",c[x]);
}
return 0;
}