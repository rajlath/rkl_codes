'''
2
3
J J F
8 9 7
5
J J J J J
5 2 4 6 3

nots = int(input())
for _ in range(nots):
    lens = int(input())
    st   = [x for x in input().split()]
    energy=[int(x) for x in input().split()]
    M = 0
    T = 0
    F = 0
    for i, v in enumerate(st):
        if v == "F":
            M += energy[i]
            T += energy[i]
            F = 1
        else:
            if v == "J":
                if F == 0:
                    M += energy[i]
                else:
                    T += energy[i]
                F = 1 - F
    print(max(M, T))

'''
nots = int(input())
for _ in range(nots):
    nol = int(input())
    foods = [x for x in input().split()]
    energies = [int(x) for x in input().split()]
    results = [0] * nol
    results[0] = energies[0]
    for i in range(1, nol):
        curr = energies[i]
        if foods[i] is "F":
            results[i] = results[i-1] + curr
        else:
            results[i] = max(results[i-2] + curr, results[i-1])
    print(results[nol-1])

