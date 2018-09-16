from math import gcd

def bits_of(m):
    """
    Binary digits of n, from the least significant bit.

    >>> list(bits_of(11))
    [1, 1, 0, 1]
    """
    n=int(m)
    while n:
        yield n & 1
        n >>= 1

def fast_exp(x,n):
    """
    Compute x^n, using the binary expansion of n.
    """
    result = 1
    partial = x
    for bit in bits_of(n):
        if bit:
            result *= partial
        partial ^= 2
    return result




MOD = int(10e9 + 7)
def expo(a, b, c):
    ans = 1
    for i in range(1, b+1):
        ans *= a
        ans %= c
    return ans

for _ in range(int(input())):
    a, b, n = [int(x) for x in input().split()]
    sums =  fast_exp(a,n)+ fast_exp(b,n)
    ans  = gcd(sums, abs(a-b)) % MOD
    print(ans)


'''
import math
nww=int(input())
for i in range(nww):
    x=int(input())
    x11=int(math.log(x)/math.log(2))
    if 2**x11==x:
        x11=x11-1
        x22=x11-2
        v1=2**x11+2**x22
        v2=2**(x11+1)+1
    else:
        xw=x-2**x11
        x22=int(math.log(xw)/math.log(2))
        if x11-x22==1:
            v1=2**x11+2**x22
            v2=2**(x11+1)+1
        else:
            v1=2**x11+2**x22
            v2=2**(x11)+2**(x22+1)

    if x==1 or x==2:
        print(3-x)
    else:
        print(min(x-v1,v2-x))
'''
'''
def gcd(a,b):
      if a == 0:
            return b
      return gcd(b % a, a)

def power(a,n,x):
      if n==0:
            return 1
      if n==1:
            return a%x
      out=power(a,n/2,x)
      bigM=(out*out)%x
      if n%2==0:
            result=bigM
      else:
            result=((a%x)*bigM)%x
      return result

p=1000000007
test=int(input())
for i in range(test):
      x=input().split()
      a=int(x[0])
      b=int(x[1])
      n=int(x[2])
      diff=a-b
      if diff==0:
            mod=(pow(a,n,p)+pow(b,n,p))%p
            print(mod)
      else:
            mod=(pow(a,n,diff)+pow(b,n,diff))%diff
            print(gcd(mod,diff)%p)
'''
