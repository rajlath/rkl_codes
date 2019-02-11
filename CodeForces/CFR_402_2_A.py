nb_pupil = int(input())
grp_1 = [int(x) for x in input().split()]
grp_2 = [int(x) for x in input().split()]
changed = 0
ans = -1
for i in range(1, 6):
    grp1 = grp_1.count(i)
    grp2 = grp_2.count(i)
    if not (grp1 + grp2) % 2:
        changed += abs(grp1 - grp2)//2
        ans = 0
    else:
        break
if ans != -1:
    print(changed//2)
else:print(-1)
