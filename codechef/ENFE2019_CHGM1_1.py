nb_test = int(input())
for _ in range(nb_test):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    max_here = 0
    max_alls = 0
    for i in arr:
            max_here += i
            if max_here == 0:
                    max_here = 0
            max_alls = max(max_alls, max_here)
    print(max_alls)



