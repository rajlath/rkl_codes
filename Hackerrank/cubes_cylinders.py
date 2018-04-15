nop, noc = [int(x) for x in input().split()]
pack_len = [int(x) for x in input().split()]
pack_cnt = [int(x) for x in input().split()]
cyl_rads = [int(x) for x in input().split()]
cyl_caps = [int(x) for x in input().split()]

cyl_diag =  [ ((2*(x * x))**0.5)//2 for x in pack_len ]
pack_lst =  list(sorted([[x,y] for x,y in zip(cyl_diag,pack_cnt)]))
cyls_lst =  list(sorted(zip(cyl_rads,cyl_caps)))


i = 0
stored = 0
d = 0
c = 0

for r, cnt in cyls_lst:
    while i < nop and cnt > 0 and pack_lst[i][1] > 0 and r > pack_lst[i][0]:
        cnt -= 1
        pack_lst[i][1] -= 1
        stored+=1
        if pack_lst[i][1] == 0: i+=1

print(stored)

