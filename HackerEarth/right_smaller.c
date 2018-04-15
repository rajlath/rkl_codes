#include"stdio.h"
int ct[2000003];
int read()
{
    int sum=0;
    char c;
    while(1)
    {
        c=getchar();
        if(c != 32 && c!= EOF) sum=sum*10+c-'0';
        else break;
        //return sum;
    }
    return sum;
}

void put(int pos)
{
    while(pos<2000003) ct[pos] ++,pos += (pos & -pos);
}


unsigned int get(int pos)
{
    unsigned int ans=0;
    while (pos > 0) ans += ct[pos],
    pos -= (pos & -pos);
    return ans;
}

int res[5000000],c=0;
void m()
{
    int n;
    n=read();
    if(n==0) return;
    n+=1000002;
    m();
    res[c++]=get(n-1);
    put(n);
}

int main()
{
m();
//for(int i=0;i<=100;i++) printf("rec[%d]=%d ",i,res[i]);
while(c--) printf("%d ",res[c]);
}