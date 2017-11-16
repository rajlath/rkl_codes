#include <stdio.h>
 
int main()
{
    int t,a,k,n,coin;
    
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&a,&k,&n);
        coin=a+k*(n-1);
        printf("%d\n", k * (n-1));
        printf("%d\n",coin);
    }
    return 0;
}
