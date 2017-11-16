decode
#include <stdio.h>
#include<string.h>
int Prime(int a)
{
    int i;
     if (a <= 1)  return 0;
    if (a <= 3)  return 1;
 
    if (a%2 == 0 || a%3 == 0) return 0;
 
    for (i=5; i*i<=a; i=i+6)
        if (a%i == 0 || a%(i+2) == 0)
           return 0;
 
    return 1;
}
int main()
{
     char str[100001];
    int t,i;
    int num,len,gn,max=0;
    
    scanf("%d",&t);
    
    while(t--)
    {
        gn=0;
        max=-1;
        scanf("%s",str);
        len=strlen(str);
        for(i=0;i<len;i++)
        {
            if(str[i]>='0' && str[i]<='9')
            {
                num=(str[i]-'0');
                i++;
                while((str[i]>='0' && str[i]<='9')&&(i<len))
                {
                    num=num*10+(str[i]-'0');
                    i++;
                }
                if(Prime(num)==1)
                {
                    gn++;
                    if(num>max)
                    max=num;
                }
            }
        }
        printf("%d %d\n",gn,max);
    }
    return 0;
}

bahubali
#include <stdio.h>
#include<stdlib.h>
#define M 1000000007
typedef unsigned long long my;
my a[1000001];
 
void get(int *x)
{
    char c =getchar_unlocked();
    for(*x=0;c>47 && c<58;c=getchar_unlocked())
        *x=*x*10+c-'0';
}
int main(void)
{
    my n,q;
    get(&n);
    get(&q);
	my i,L,R;
	for(i=1;i<=n;i++)
		get(a+i),a[i]=(a[i]+a[i-1]);
	while(q--)
	{
		get(&L);
		get(&R);
		printf("%llu\n",(a[R]-a[L-1])/(R-L+1));
	}
 
    return 0;
}

Diwali
#include <stdio.h>
 
int main()
{
    int t,a,k,n,coin;
    
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&a,&k,&n);
        coin=a+k*(n-1);
        printf("%d\n",coin);
    }
    return 0;
}

diwali palindrome
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;
    
#define FOR(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define SZ(c) ((int)(c).size())
    
typedef long long LL;
    
int main(void) {
    int T;
    scanf("%d", &T);
    assert(1 <= T && T <= 100);
    while(T--) {
        LL n;
        cin >> n;
        assert(1 <= n && n <= 1e12);
        vector<int> B;
        B.push_back(0);
        int m=0;
        while(n>0) {
            ++m;
            //try 'a'
            LL p = m-B.back();
            if(SZ(B)>=2) p += (m-B.back() <= B.back()-B[SZ(B)-2]-1);
            if(SZ(B)>=3) p += (m-B.back() <= B[SZ(B)-2]-B[SZ(B)-3]-1);
            if(p <= n) { n -= p; continue; }
            //try 'b'
            p = 1;
            if(SZ(B)>=2) p += 1;
            if(p <= n) { n -= p; B.push_back(m); continue; }
            //try 'c' (assert n == 1)
            p = 1;
            if(p <= n) { n -= p; continue; }
        }
        printf("%d\n", (int)m);
    }
    return 0;
}

probability
#include <stdio.h>
l, t = [int(x) for x in input().split()] 
for i in range(l):


 
int main()
{
    long long int l,t,count=0,i,j,s,total;
   scanf("%ld %ld",&l,&t); //cin>>l>>t;
    
    long long int a[l];
    for(i=0;i<l;i++)
    {
       scanf("%ld",&a[i]); //cin>>a[i];
    }
    for(i=0;i<l;i++)
    {
        if(a[i]<=t) 
        {
        count++;s=a[i];j=i+1;
        while(s<=t && j<l)
        {
            s+=a[j];
            if(s<=t) count++;
            j++;
        }
        
    }
    }
    total=(l*(l+1))/2;
    double ans=(double)count/total;
    printf("%g",ans);//cout<<(double)count/total<<endl;
    
}

probability
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
struct Node 
{
    int count;
    struct Node *a[26];
};
 
int main()
{
    struct Node *head,*temp;
    int i,n,j,len,flag;
    char str[22];
    char op[22];
    
    head=(struct Node *)malloc(sizeof(struct Node));
    
    head->count=0;
    for(i=0;i<26;i++)
    head->a[i]=NULL;
    
    scanf("%d",&n);
    while(n--)
    {
        scanf("%s",op);
        scanf("%s",str);
        
        if(strcmp(op,"add")==0)
        {
            len=strlen(str);
            temp=head;
            for(i=0;i<len;i++)
            {
                //printf("%d ",temp->count);
                if(temp->count==0)
                {
                    temp->count=temp->count+1;
                    temp->a[str[i]-'a']=(struct Node *)malloc(sizeof(struct Node));
                    temp=temp->a[str[i]-'a'];
                    temp->count=0;
                    for(j=0;j<26;j++)
                    temp->a[j]=NULL;
                }
                else
                {
                    temp->count=temp->count+1;
                    if(temp->a[str[i]-'a']==NULL)
                    {
                        temp->a[str[i]-'a']=(struct Node *)malloc(sizeof(struct Node));
                        temp=temp->a[str[i]-'a'];
                        temp->count=0;
                        for(j=0;j<26;j++)
                        temp->a[j]=NULL;
                    }
                    else
                    temp=temp->a[str[i]-'a'];
                }
            }
            temp->count=1;
            //printf("\n");
        }
        else
        {
            len=strlen(str);
            temp=head;
            flag=0;
            for(i=0;i<len;i++)
            {
                if(temp->a[str[i]-'a']==NULL)
                {
                    printf("0\n");
                    flag=1;
                    break;
                }
                else
                {
                    temp=temp->a[str[i]-'a'];
                }
                
            }
            if(flag==0)
            printf("%d\n",temp->count);
        }
    }
    return 0;
}
trump
#include<bits/stdc++.h>
#define MOD 1000000007
 
 
using namespace std;
typedef long long ll;
 
ll fac[1000006];
 
void init(){
    fac[0] = 1;
    for(int i=1;i<1000002;i++){
        fac[i] = (fac[i-1]*i)%MOD;
    }
}
 
ll modpow(ll a, ll b){
    if(b==0) return 0;
    if(b == 1) return a;
    if(b&1) return (a*modpow(a, b-1))%MOD;
    ll k = modpow(a, b/2);
    return (k*k)%MOD;
}
 
ll inv(ll a){
    return modpow(a, MOD-2);
}
 
ll stirling(ll n, ll m){
    if(n==m or m == 1) return 1;
    ll ans = 0;
    for(ll i=1;i<=m;i++){
        ll temp = (((fac[m]*inv(fac[m-i]))%MOD)*(inv(fac[i])))%MOD;
        temp = (temp*modpow(i, n))%MOD;
        if((m-i)&1) temp *= -1;
        ans = (ans+temp)%MOD;
    }
    ans = (ans*inv(fac[m]))%MOD;
    return ans;
}
 
int main(){
	ios::sync_with_stdio(false);
	#ifdef DBG
		freopen("in", "r", stdin);
	#endif
    
    init();
    
    ll n, m;
    cin>>n>>m;
    
    ll ans = stirling(n-2, n-m);
    
    
    
    ll temp = (((fac[n]*inv(fac[n-m]))%MOD)*(inv(fac[m])))%MOD;
    temp = (temp*fac[n-m])%MOD;
    ans = (temp*ans)%MOD;
    if(ans < 0) ans += MOD;
    cout<<ans<<"\n";
    
	return 0;
}
1000
4952 64342 72178   349050190    349050190
23391 28544 16938  483473119    483473119 
60483 54634 92690  5064031309   769064013 
30164 65790 39509  2599261484   -1695705812
69328 34185 30121  1029721528   1029721528
1114 96072 76759 
4331 39117 31650 
58722 61260 17762 
2933 24261 15096 
61464 73154 84104 
9678 29174 85744 
38458 40618 23023 
4464 71135 80623 
10074 90567 99011 
1540 92409 26557 

4644017486
483473119
5064031309
2599261484
1029721528
7374295690
1238018264
1088097582
366222728
6152532326
2501475960
935146054
5735050434
8967048744
2454014944

349050190
483473119
769064013
-1695705812
1029721528
-1215638902
1238018264
1088097582
366222728
1857565030
-1793491336
935146054
1440083138
377114152
-1840952352
-2059379463
