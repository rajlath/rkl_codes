'''
#include<stdio.h>
int main()
{
    int n,i,j,arr[902],pre[901],ans=0;
    scanf("%d%d",&n,&arr[0]);
    pre[0]=arr[0];
    for(i=1;i<n;i++)
{
    scanf("%d",&arr[i]);
    pre[i]=arr[i]+pre[i-1];
}
    for(i=0;i<n-1;i++)
{
    for(j=i+1;j<n;j++)
{
    int k;
       for(k=i;k<j;k++)
       {
    if((pre[i]^(pre[j]-pre[k]))>ans)
    ans=pre[i]^(pre[j]-pre[k]);
        if((arr[i]^(pre[j]-pre[k]))>ans)
    ans=arr[i]^(pre[j]-pre[k]);
       }
}
}
printf("%d",ans);
return 0;
}
4
1 2 1 3
'''
noe = int(input())
pre = [0] * (noe + 1)
arr = [int(x) for x in input().split()]
pre[0] = arr[0]
for i in range(1, noe):
    pre[i] = arr[i] + pre[i-1]
ans = 0
for i in range(1, noe-1):
    for j in range(i+1, noe):
        for k in range(i, j):
            var1 = pre[i] ^ (pre[j] - pre[k])
            ans = max(ans, var1)
            print(var1, ans, pre[i], pre[j], pre[k])
            var2 = arr[i] ^ (pre[j] - pre[k])
            ans = max(ans, var2)
            print(var2, ans)
print(ans)



