nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    arrs = [100] + [int(x) for x in input().split()]
    cnt = 0
    for i in range(1, lens + 1):
            if arrs[i] < lens + 1 and arrs[i] > 0:
                    if arrs[arrs[i]] != i:
                            cnt += 1


    print(cnt)