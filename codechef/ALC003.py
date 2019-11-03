for _ in range(int(input())):
    nb = int(input())
    balances = [int(x) for x in input().split()]
    avgbal =  sum(balances) // nb
    needed = 0
    for i in range(nb - 1):
        curr = balances[i]
        diff = abs(curr - avgbal)
        if curr > avgbal:
            balances[i + 1] = balances[i + 1] + diff
        elif curr < avgbal:
            balances[i + 1] = balances[i + 1] - diff
        needed += diff
    print(needed)
