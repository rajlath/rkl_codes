'''
1
15 2 3 5


for _ in range(int(input())):
    n, a, b, c = [int(x) for x in input().split()]
    sieve = set()
    primes = [a, b, c]
    for i in primes:
        x = i
        while x <= n:
            sieve.add(x)
            x+=i
                       
    
    print(len(sieve))

long int gcd(long int a,long int b)
{
   
 
 
    
 
     if (b!=0)
        return gcd(b, a%b);
        else
        return a;
    
}
long int lcm(long int a,long int b)
{
    return (a*b)/gcd(a,b);
}
int main()
{
    //printf("Hello World!\n");
    int t;
    scanf("%d",&t);
    while(t--)
    {
        long int n,a,b,c,count=0;
        scanf("%ld %ld %ld %ld",&n,&a,&b,&c);
        count+=n/a;
        count+=n/b;
        count+=n/c;
        long long int x=lcm(b,c);
        count+=n/lcm(a,x);
        count-=n/lcm(a,b);
        count-=n/x;
        count-=n/lcm(a,c);
        
        printf("%ld\n",count);
    }
    return 0;
}
'''

def gcd(a, b) :
    if b != 0:
        return gcd(b, a%b)
    else:
        return a
        
def lcm(a, b):
    return int((a*b)/gcd(a,b))
    
for _ in range(int(input())):
    count = 0
    n,a, b, c = [int(x) for x in input().split()]
    lst = [a, b, c]
    for i in lst:
        count += n//i
    x=lcm(b,c)
    count+=n//lcm(a,x);
    count-=n//lcm(a,b);
    count-=n//x;
    count-=n//lcm(a,c); 
    print(count)   
        
    
    
  
    
