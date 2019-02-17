n,b=map(int,input().split())

pf=[]
i=2
while i*i<=b:
    if b%i==0:
        aa=0
        while b%i==0:
            b=b//i
            aa+=1
        pf.append([i,aa])
    i+=1
if b!=1:
    pf.append([b,1])

ar=[]
for i in range(len(pf)):
    a=0
    ch=n
    b=pf[i][0]
    while n>=b:
        a+=n//b
        b=b*pf[i][0]
    ar.append(a//pf[i][1])
    n=ch

print(min(ar))