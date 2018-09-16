def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n/3-correction) if sieve[i]]
import sys
primes = primes2(1000000)
print(primes[12345])


def primes(a,b):
    x=[]
    for i in range(a,b+1):
        p=True
        if i==1:
            p=False
        elif i==2 or i==3:
            p=True
        elif(i%2==0 or i%3==0):
            p=False
        else:
            for j in range(5,int((i)**(0.5)+1),6):
                if i%j==0 or i%(j+2)==0:
                    p=False
                    break
        if p==True:
            x.append(i)
    return x

a,b=map(int,input().split())
x=primes(a,b)
for obj in x:
    print(obj)
