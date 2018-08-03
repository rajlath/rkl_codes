members  = {}
counts   = {}
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a == 1:
        members[b]  = members.get(b, 0) + 1
        cnt = members[b]
        counts[cnt] = counts.get(cnt, 1) + 1
        if cnt-1 in counts:
            counts[cnt-1] -= 1
            if counts[cnt-1] < 1:
                del counts[cnt-1]
    elif a == 2:
        if b in members:
            had = members[b]
            members[b] -= 1
            cnt = members[b]
            if members[b] < 1:
                del members[b]
            if had in counts:
                counts[had] -= 1
                if counts[had] < 1:del counts[had]
            counts[cnt] = counts.get(cnt, 0) + 1

    else:
        print(1 if b in counts else 0)
    print(members)
