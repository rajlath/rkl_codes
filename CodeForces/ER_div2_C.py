n, m = [int(x) for x in input().split()]
vals = [int(x) for x in input().split()]
diff = [y-x for x, y in zip(vals, vals[1:])]
print(diff)
diff = sorted(diff)
print(diff)
print(sum(diff[:n-m]))
