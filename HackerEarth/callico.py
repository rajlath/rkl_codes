'''
2
4
abcd
8
abcdcdab
'''
for _ in range(int(input())):
    noe = int(input())
    part= noe // 4
    s = input()
    x = 0
    a = s[x:part+x]
    x += part
    b = s[x:part+x]
    x += part
    c = s[x:part+x]
    x += part
    d = s[x:part+x]
    first = set(sorted(a)) - set(sorted(d))
    second= set(sorted(c)) - set(sorted(b))

    diffs1 = len(first)
    diffs2 = len(second)
    print(diffs1,diffs2, first, second)

    diff = diffs1 + diffs2
    if diff == 0:
        print("YES")
    else:
        print("NO", diff)
