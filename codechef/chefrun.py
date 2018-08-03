'''
3
1 3 2 1 2
1 5 2 1 2
1 5 3 2 2
Example Out
Kefa
Chef
Draw
'''
for _ in range(int(input())):
    posc, posk, posx, velc, velk = [int(x) for x in input().split()]
    ans = 0
    ct = (posx - posc) / velc
    kt = (posk - posx) / velk
    if ct > kt : ans = 1
    if kt > ct : ans = 2
    print(['Draw','Kefa','Chef'][ans])