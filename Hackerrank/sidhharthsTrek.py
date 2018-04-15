'''
10
10
0 1612 343 493 261 177 476 2900 1570 618
10
0 1353 1077 2948 3045 630 870 1515 752 72
10
0 599 1688 974 710 1735 258 220 1696 11
10
0 368 1676 201 875 462 1026 2983 2245 650
10
0 1549 448 567 1518 1576 3016 2799 2035 706
10
0 1456 1284 507 2899 2049 19 384 2041 2043
10
0 1092 2584 1413 2266 16 2559 240 2163 2097
10
0 1579 659 2200 1632 1062 134 1429 220 1837
10
0 501 1277 53 646 145 2251 1789 1106 557
10
0 1733 2658 635 1373 408 3022 2749 1513 1655
IMPOSSIBLE
IMPOSSIBLE
IMPOSSIBLE
POSSIBLE
POSSIBLE
POSSIBLE
POSSIBLE
IMPOSSIBLE
IMPOSSIBLE
POSSIBLE
'''
for _ in range(int(input())):
    noe = int(input())
    camps = [int(x) for x in input().split()]
    camps = [int(x) for x in camps if x <= 3048]
    camps = sorted(camps)
    if camps[-1]<3048: camps.append(3048)
    if camps[-1] - camps[-2] > 500:
        print("IMPOSSIBLE")
    else:
        ans = "POSSIBLE"
        for i in range(1, len(camps)):
            if camps[i] - camps[i-1] >= 1000:
                ans = "IMPOSSIBLE"
                break
            if camps[i]>=3048:
                break
        print(ans)