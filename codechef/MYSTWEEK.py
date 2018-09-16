for i in range(int(input())):
    nod, ntask = [int(x) for x in input().split()]
    dtasks = [int(x) for x in input().split()]
    done = False
    while ntask > 0:
        for i in range(1, nod+1):
            if ntask <= dtasks[i-1]:
                print(i)
                done = True
                break
            ntask -= dtasks[i-1]
        if done:break

