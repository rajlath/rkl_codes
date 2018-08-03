n, k = [int(x) for x in input().split()]
knights = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]
knight_coin = []
for i in range(n):
    knight_coin.append([knights[i], coins[i]])
knight_coin = sorted(knight_coin,key=lambda x:(x[0],-x[1]))
kc = {}
for i in range(n):
    curr = coins[n - i -1]
    for j in range(k):
        if j > -1:
            curr += knight_coin[knights[i]][1]
    print(curr)





