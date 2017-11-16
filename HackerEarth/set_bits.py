'''
LL maxi = 1000000000000000000;
int main()
{
    int t;
    scanf("%d",&t);;
    assert(t and t<=10e5);
    while(t--){
        LL n;
        scanf("%lld",&n);
        assert(n and n<=maxi);
        LL ans=0;
        LL cur=2;
        bool flag=true;
        int times=1;
        while(flag){
            int div=times;
            while(flag and div){
                LL t=cur+(cur>>div);
                if(t<=n){
                    ans+=t;
                    ans%=mod;
                }
                else{
                    flag=false;
                    break;
                }
                div--;
            }
            cur=cur<<1;
            times++;
        }
        printf("%lld\n",ans);
    }
    return 0;
}
'''
mod = 10e18
t = int(input())
while(t):
    n  = int(input())
    ans=0
    cur=2
    flag=True
    times=1

    while(flag):
        div=times;
        while(flag and div):
            t1=cur+(cur>>div);
            if(t1<=n):
                ans+=t1
                ans%=mod
            else:
                flag=False
                break
            div-=1
        cur=cur<<1
        times+=1
    print(int(ans))
    t-=1








