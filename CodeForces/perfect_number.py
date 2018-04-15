def dig_sum(n):
    r = 0
    while n:
        n, re = divmod(n, 10)
        r += re
        if r>10:
            break
    return r

n = int(input())
ans=10
for i in range(n):
    while(True):
        ans+=9
        if dig_sum(ans)==10:
            break
print(ans)

