from collections import Counter as C
from fractions import gcd

n=input()
a=map(int,raw_input().split())
b=map(int,raw_input().split())
dic=C();toAdd=0
for i in xrange(n):
    A,B=a[i],b[i]
    if A==0:
        toAdd+=(B==0)
        continue
    g=gcd(A,B)
    dic[(B/g,A/g)]+=1
print dic.values(), toAdd
print max(dic.values()+[0])+toAdd