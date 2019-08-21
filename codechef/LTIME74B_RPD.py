def dig_sum(n):
    if n == 0:return 0
    return n % 10 + dig_sum(n // 10)

for _ in range(int(input())) :
    lens = int(input())
    arrs = [int(x) for x in input().split()]
    maxs = 0
    for i in range(lens):
        for j in range(i+1, lens):
            maxs = max(maxs, dig_sum(arrs[i] * arrs[j]))
    print(maxs)
