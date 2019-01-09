n , k = [int(x) for x in input().split()]
ans = n // (k-1)
if ans == 0:
    ans = 1
    ans *= k
    ans += k - 2
else:
    ans *= k
    ans += (k-1)
print(ans)





