import math
nb_airdrops = int(input())
BM, DM, UM = [int(x) for x in input().split()]
BA, DA, UA = [int(x) for x in input().split()]
BF = BM * BA
DF = DM * DA
UF = UM * UA
impact = {"BAGGI":BF, "DACIA":DF, "UAZ":UF}
impact = sorted(impact.items(), key=lambda x: x[1])

#print(impact)

for _ in range(nb_airdrops):
    needed = int(input())
    ans  = "NO"
    for k, v in impact:
        if needed <= v:
            ans = k
            break

    print(ans)


