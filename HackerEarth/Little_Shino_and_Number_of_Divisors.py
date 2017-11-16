n,a = input(),[int(x) for x in input().split()]
ans = 1
mod = 10**9 + 7
for item in a:
    ans = (ans * (item+1) ) % mod
ans = (ans*pow(2,mod-2,mod))%mod

res = 1
for item in a:
    res =( res * (item*ans+1) )% mod
    
print (res)
