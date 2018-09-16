nb_sqr = int(input())
sqr_side = [int(x) for x in input().split()]
ans = 0
if nb_sqr ==1 :
    ans = (4 * sqr_side[0])
else:
    distances = [int(x) for x in input().split()]
    for i in range(nb_sqr-1):
         ans += (5 * sqr_side[i]) + distances[i]
    ans += (4 * sqr_side[nb_sqr-1])
print(ans)
