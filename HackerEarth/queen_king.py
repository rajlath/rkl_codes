from collections import Counter
import math
for _ in range(int(input())):
    noe = int(input())
    part= noe // 4
    s = input()
    x = 0
    a = Counter(s[x:part+x])
    x += part
    b = Counter(s[x:part+x])
    x += part
    c = Counter(s[x:part+x])
    x += part
    d = Counter(s[x:part+x])


    print(a, b, c, d)
    print(a - d)
    diffs1 = len(a - d)
    diffs2 = len(c - b)


    diff = diffs1 + diffs2
    if diff == 0:
        print("YES")
    else:
        print("NO", diff)