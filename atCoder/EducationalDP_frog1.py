INF = 1 << 60
nb_stones = int(input())
heights   = [int(x) for x in input().split()]
DP = [INF for _ in range(nb_stones)]
DP[0] = 0
DP[1] = DP[0] + abs(heights[1] - heights[0])
for i in range(1, nb_stones):
    DP[i] = min(DP[i-1] + abs(heights[i] - heights[i-1]), DP[i-2] + abs(heights[i] - heights[i-2]))
print(DP[nb_stones - 1])