def get_cycle_length(x):
    lens = 0
    while x != 1:
        if x % 2 == 0:x >>= 1
        else:x = x * 3 + 1
        lens += 1
    return lens + 1

def solve(a, b):
    maxs = 0
    a, b = min(a, b), max(a, b)
    for i in range(a, b + 1):
        maxs = max(get_cycle_length(i), maxs)
    return maxs

while True:
    try:
        a, b = [int(x) for x in input().split()]
        ans = solve(a, b)
        print(a, b, ans)
    except:
        break





