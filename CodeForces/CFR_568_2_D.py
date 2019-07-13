def isValidAP(arrs):
    x = [(x[i][0]-x[i-1][0]) for i in range(1, len(x))]
    return all(i == x[0] for i in x)


lens = int(input())
arrs = [int(x) for x in input().split()]
brrs = sorted([(arrs[i], i + 1) for i in range(lens)])
if isValidAP(brrs[1:]):
    print(brrs[0][1])
elif isValidAP(brrs[:-1]):
    print(brrs[-1][1])
else:
    diff = (brrs[-1][0] - brrs[0][0]) // 2
    x = []
    if brrs[0][0] + (lens - 2) * d != brrs[-1][0]:
        x.extend([1, 2])
    i = 1
    while i < n:
        if brrs[i][0] - b[i - 1][0] == d:
            i += 1
            continue
        else:
            v = brrs[i - 1][0]
            while b[i][0] - v != d:
                x.append(b[i][1])
                i += 1
                if i >= n:
                    x.append(1)
                    break
            i += 1
    if len(x) == 0:print(0)
    elif len(x) == 1:print(x[0])
    else:print(-1)
