denos =[20,50,100,200, 500,1000]
for _ in range(int(input())):
    ins, out = [int(x) for x in input().split()]
    returns  = out - ins
    if returns in denos:
        print(0)
    else:
        hassol = False
        for i in denos:
            maybe = i - returns
            if maybe > 0 and maybe < 10:
                print(maybe)
                hassol = True
                break
        if not hassol:print(-1)



