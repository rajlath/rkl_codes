import fileinput
f = fileinput.input()

T = int(f.readline())
for case in range(1, T+1):
    D, N = (int(x) for x in f.readline().split())
    K, S = list(), list()
    for i in range(N):
        k, s = (int(x) for x in f.readline().split())
        K.append(k)
        S.append(s)

    arrival = max((D-k) / s for (k, s) in zip(K, S))
    solution = speed = D / arrival
    print("Case #%d: %.6f" % (case, solution))
    #print(f"Case #{case}: {solution}")