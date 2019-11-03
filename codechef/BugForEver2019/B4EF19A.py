for _ in range(int(input())):
    raw, hunger, cost = [int(x) for x in input().split()]
    restore = hunger // 2 + hunger % 2
    ans = [raw - 8 * cost, raw - restore][8 * cost >= restore]
    print([0, ans // 3][ans > 0])