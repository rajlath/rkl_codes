nos, needed = [int(x) for x in input().split()]
diff = []
have = 0
for i in range(nos):
    a, b = [int(x) for x in input().split()]
    have += a
    diff.append(a - b)
diffs = sorted(diff, reverse = True)
for i in range(nos):
    if have <= needed:
        print(i)
        exit()
    have -= diffs[i]
if have <= needed:
    print(nos)
else:
    print(-1)





