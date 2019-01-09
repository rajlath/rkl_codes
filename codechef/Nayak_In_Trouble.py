nb_Test = int(input())
for _ in range(nb_Test):
    lens =  int(input())
    arrA =  [int(x) for x in input().split()]
    arrB =  [int(x) for x in input().split()]
    u = 1
    v = 1
    mx= 0
    while u < lens and v < lens:
        if arrA[u] <= arrB[v] and u <= v:
            mx = max(mx, v - u)
            v += 1
        else:
            u += 1
            v += 1
    print(mx)


