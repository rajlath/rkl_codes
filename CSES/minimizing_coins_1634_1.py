def coin_change(coins, N):
    M = len(coins) # number of coins
    Num = [[float('inf') for _ in range(N + 1)] for i in range(M + 1)]
    for m in range(M + 1):
        for n in range(N + 1):
            # m = 0: no coins used
            # n = 0: amount is 0
            if m == 0 or n == 0:
                continue
            if n == coins[m - 1]:
                Num[m][n] = 1
            if coins[m - 1] <= n:
                Num[m][n] = min( Num[m][n], Num[m - 1][n], Num[m][n - coins[m - 1]] + 1)
            else:
                Num[m][n] = Num[m - 1][n]

    return -1 if Num[M][N] == float('inf') else Num[m][n]

def coin_change_optimized(coins, N):
    Num = [float('inf') for _ in range(N + 1)]
    #0 coins needed when the amount is 0
    Num[0] = 0
    for n in range(N + 1):
        for coin in coins:
            if coin <= n:
                Num[n] = min(Num[n], Num[n - coin] + 1)
    return -1 if Num[N] == float('inf') else Num[n]

nb_coin, amount = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]
print(coin_change_optimized(coins, amount))