'''
1
4 4
1 2 3 4
1 4 5 3
'''
for _ in range(int(input())):
    nofs, nobs = [int(x) for x in input().split()]
    needed = [int(x) for x in input().split()]
    blessing= [int(x) for x in input().split()]
    pass_cnt = 0
    bless_cnt = 0
    for i in needed:
        may_need = []
        for j in blessing:
            if i%j==0:
                may_need.append(j)
        #print(may_need)
        if len(may_need)>=1:
            bless_cnt += i // max(may_need)
            pass_cnt += 1
    print(pass_cnt, bless_cnt)


