'''
#include <stdio.h>
//#include <math.h>
#define TAG 987654321
#define MOD 1000000000
/*
111111111
119357639
380642361
388888889
611111111
619357639
880642361
888888889
*/
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
'''
n = int(input())
if  n <= 8: print("0")
elif n == 9: print("8")
else:
    print("72" + "0" * (n - 9 -1))




