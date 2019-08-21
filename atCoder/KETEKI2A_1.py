n = int(input())
water = [int(x) for x in input().split()]
sum1 = sum(water)
sum2 = sum([v for i, v in enumerate(water) if i%2==1])

ans = [0] * n
ans[0] = sum1 - 2 * sum2
for i in range(1, n ):
    ans[i] = (water[i - 1] - ans[i - 1]//2) * 2
print(*ans)    