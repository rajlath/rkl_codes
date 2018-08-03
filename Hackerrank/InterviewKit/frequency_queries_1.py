
members = {}
counts   = {}
for _ in range(int(input())):
    a, b = [int(x) for x in input().split()]
    if a == 1:
        members[b] = members.get(b, 0) + 1
        cnt = members[b]
        counts[cnt] = counts.get(cnt, 0) + 1
        if cnt - 1 in counts:
            counts[cnt-1] -= 1
            if counts[cnt-1] < 1: del counts[cnt-1]
    if a == 2:
        if b in members:
            was = members[b]
            members[b] -= 1
            if members[b] < 1:del members[b]
            if was in counts:
                counts[was] -= 1
                if counts[was] < 1: del counts[was]
            counts[was-1] = counts.get(was-1, 0) + 1
    if a == 3:
        print(1 if b in counts else 0)
