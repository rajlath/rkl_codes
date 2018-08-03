noh, d = [int(x) for x in input().split()]
hotels    = [int(x) for x in input().split()]
ans = 2
for i in range(noh-1):
    curr_diff = hotels[i+1] - hotels[i]
    if curr_diff > d*2:
        ans += 2
    elif curr_diff == d*2:
        ans += 1
print(ans)

print( 2 + sum([(b - a >= 2*d) + (b - a > 2 * d) for a, b in zip(hotels, hotels[1:])]))











