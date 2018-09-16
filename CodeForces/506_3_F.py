a,b = map(int,raw_input().split())
d1,d2 = 1,1
n = a+b
ans = pow(10,16)
for i in range(1,int(pow(n,0.5))+1):
    if a%i==0:
        d1 = i
    if b%i==0:
        d2 = i
    if n%i==0:
        if a/d1<=n/i or b/d2<=n/i:
            ans = min(ans,2*(i+(n/i)))
print ans