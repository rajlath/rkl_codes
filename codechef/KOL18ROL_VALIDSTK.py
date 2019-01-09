nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    stak = 0
    ops  = [int(x) for x in input().split()]
    ans = "Valid"
    for i in ops:
        if i == 1:
            stak+=1
        else:
            stak-= 1
        if stak < 0:
            ans = "Invalid"
            break
    print(ans)    