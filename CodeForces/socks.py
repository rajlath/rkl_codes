d, m  = [int(x) for x in input().split()]
x = d
ans = d
while x > 1:
    x, a  =  divmod(x, m)    
    ans += x
    print(x, a, ans)
print(ans)    

