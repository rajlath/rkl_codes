m, n =map(int, raw_input().split())
coins = sorted([int(i) for i in raw_input().split()])

def Changes(n, coins):
    counts = [1] + [0] * n
    for c in coins:
        for i in range(len(counts)):
            if c + i <= n:
                counts[i + c] += counts[i]
    return counts[-1]

print Changes(n, coins)