for _ in range(int(input())):
    lens, broken = [int(x) for x in input().split()]
    pots = [int(x) for x in input().split()]
    brokens = [int(x) for x in input().split()]
    ok = []
    broke = []
    for i in pots:
        if i in brokens:
            broke.append(i)
        else:
            ok.append(i)
    answer = ok + broke
    print(*answer)