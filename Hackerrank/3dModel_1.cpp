#include <stdio.h>
#include <memory.h>
#define maxn 105

int arr[maxn][maxn],m,n;
int flag[maxn][maxn];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //freopen("in.txt","r",stdin);
    int ud=0,max=0;
    while(~scanf("%d%d",&m,&n))
    {
        getchar();
        for(int i=1; i<=m; i++)
        {
            for(int j=1; j<=n; j++)
            {
                char temp;
                temp=getchar();
                arr[i][j]=temp-'0';
                if(arr[i][j]>0) ud++;
                max=max>arr[i][j]?max:arr[i][j];
            }
            getchar();
        }
        long long sum=2*ud;
        for(int i=0; i<max; i++)
        {
            memset(flag,0,sizeof(flag));
            for(int i=1; i<=m; i++)
                for(int j=1; j<=n; j++)
                    if(arr[i][j]>0) flag[i][j]=1;
            for(int i=1; i<=m; i++)
                for(int j=1; j<=n; j++)
                {
                    if(flag[i][j])
                    {
                        if(flag[i-1][j]==0) sum++;
                        if(flag[i][j-1]==0) sum++;
                        if(flag[i+1][j]==0) sum++;
                        if(flag[i][j+1]==0) sum++;
                    }
                }
            for(int i=1; i<=m; i++)
                for(int j=1; j<=n; j++)
                    arr[i][j]--;
        }
        printf("%lld\n",sum);
    }
    return 0;
}
