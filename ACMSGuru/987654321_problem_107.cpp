
#include <stdio.h>

#define TAG 987654321
#define MOD 1000000000

int main()
{
    int n;
    scanf("%d",&n);
    if(n<=8)
        printf("0");
    else if(n==9)
        printf("8");
    else
    {
        printf("72");
        for(int i=n-9-1;i;--i)
            printf("0");
    }
    return 0;
}
