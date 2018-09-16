nov, nop = [int(x) for x in input().split()]
votes = {}
coins = {}
for i in range(nov):
    a, b = [int(x) for x in input().split()]
    votes[a] = (votes.get(a, 0) + 1)
    coins[a] = (coins.get(a, 0) + b)
needed = (nov // nop) + 1
coins  = [coins[x] for x in coins if x != 1]
print(sorted(coins))
if 1 in votes:
    if votes[1] >= needed:
        print(0)
    else:
        print(1)




