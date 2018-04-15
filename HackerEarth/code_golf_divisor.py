r=range
for i in r(1,101):
    c=[1]
    for j in r(2,i+1):
        if not i%j:c.append(j)
    print(*c)

'''
r,i=range,input
for t in r(i()):h,d,s=map(int,raw_input().split());x=[i() for _ in r(i())];print "NY"[d/s+sum(x)<=h**0.5/4]

r,i,j=range,input,int
for _ in r(j(i())):
    h,d,s=map(j,i().split())
    x=0
    for _ in r(j(i())):x+=j(i())
    print("NY"[h**0.5/4-d/s-x>=0])

n,s=input().split()
n,l=int(n),len(s)
k=P=1
while k<n+1:h=-k%l;print(s[h:]+s[:h] if P%k else k);P*=k*k;k+=1

t,r=raw_input().split()
print 1
x=len(r)
for a in xrange(2,1+int(t)):print r[x-a%x:]+r[:x-a%x] if all(a%i for i in xrange(2,a)) else a

N,m=1005,10**9+7
F=[[1]*N for i in range(N)]
for i in range(N):
  s=1
  for j in range(2,N):
    F[i][j],s=(s+m)%m,s*2
    if j>i:s-=F[i][j-i]
for t in range(input()):
  f,n=map(int,raw_input().split())
  print F[f][n]

import collections as c
r,i,N=range,input,1001
R=r(N)
m=[[0 for w in R] for j in R]
for f in R:
 q,s=c.deque([0]*(f-1)),1;q.append(1)
 for n in R:m[f][n]=q[-1];q.append(s);s=(2*s-q.popleft())%1000000007
for tc in r(int(i())):f,n=map(int,i().split());print(m[f][n-1])


'''