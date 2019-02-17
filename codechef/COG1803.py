nb_Test = int(input())
for _ in range(nb_Test):
    lens = int(input())
    votes = [int(x) for x in input().split()]
    ayes = 0
    nyes = 0
    for i in votes:
        ayes += i == 1
        nyes += i == -1
    if ayes >= nyes:
        print("YES")
    else:
        print("NO")