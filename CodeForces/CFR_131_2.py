n, m = [int(x) for x in input().split()]
print(sum([((a * a) + b == n) and ((b * b) + a == m) for a in range(40) for b in range(40)]))
