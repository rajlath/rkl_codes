for _ in range(int(input())):
    lens, k = [int(x) for x in input().split()]
    arrs = [int(x) for x in input().split()]
    buff = []
    while len(arrs) >= k:
        lens = len(arrs)
        for i in range(lens // k + 1):
            begin = i * k
            ends  = i * k + k
            if ends <= lens:
                curr = sum(arrs[begin:ends])
                buff.append(curr)
            else:
                buff = buff + arrs[begin:]
        arrs = [x for x in buff]
        buff = []
    print(*arrs)








