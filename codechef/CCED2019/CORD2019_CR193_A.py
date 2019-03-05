'''
2
14
abcuodfegrheyd
10
codeeerdee
'''
nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    ins  = list(input())
    tgt  = list("codered")
    i = 0
    while ins:
        curr = ins.pop()
        if curr == tgt[-1]:
            tgt.pop()
        if not tgt:break
    print(["yes", "no"][len(tgt)>0])