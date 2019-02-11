x, y, z = [int(x) for x in input().split()]
g, p, b = [int(x) for x in input().split()]
ans = "YES"
if x > g:
    ans = "NO"
else:
    g -= x
    if g + p < y:
        ans = "NO"
    else:
         if g + p - y + b < z:
             ans = "NO"
print(ans)
