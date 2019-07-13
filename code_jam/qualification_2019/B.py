'''
Input
2
2
5

output
SE
EESSSESE


Case #1: ES
Case #2: SEEESSES
'''
nb_test = int(input())
for indx in range(1, nb_test+1):
    lens = int(input())
    ins = input()
    ans = ''
    for i in ins:
        if i == "E":ans += "S"
        else:ans += "E"
    print("Case #{}: {}".format(indx, ans))




