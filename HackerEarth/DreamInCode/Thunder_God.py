
for _ in range(int(input())):
    coins, max_pick = [int(x) for x in input().split()]
    a = [1] * (coins + 1)
    i = 1
    while i <= coins:
        a[i] = 0
        i += (max_pick + 1)
    print(["PLAY", "NOPLAY"][a[coins]==0])

