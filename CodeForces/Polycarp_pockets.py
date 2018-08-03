from collections import Counter
noc = int(input())
coins=[int(x) for x in input().split()]
coinC = Counter(coins)
print(coinC.most_common()[0][1])

