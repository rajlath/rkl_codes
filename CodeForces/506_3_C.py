noe = int(input())
arr = [[int(x) for x in input().split()] for i in range(noe)]
aL  = sorted(arr, reverse=True)
aR  = sorted(arr, key = lambda x: x[1], reverse=True)
if aL[0] == aR[noe-1]:
    print(max(0, aR[noe-2][1] - aL[1][0]))
else:
    print(max(0, aR[noe-2][1] - aL[0][0], aR[noe-1][1] - aL[1][0]))