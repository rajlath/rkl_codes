'''
2
6 0
1 1 1 1 1 1
5 1
2 4 6 3 4
'''
for _ in range(int(input())):
    noe, limit = [int(x) for x in input().split()]
    arr =  [int(x) for x in input().split()]
    mscores = arr[::2]
    tscores = arr[1::2]
    mval = sum(mscores)
    tval = sum(tscores)
    if tval > mval :
        print("YES")
        break
    else:
        mscores = sorted(mscores)[::-1]
        tscores = sorted(tscores)
        limit = min(noe//2, limit)
        for i in range(limit):
            if mscores[i] > tscores[i]:
                tval += 2 * ( mscores[i] - tscores[i])
            else:break
    print(["NO", "YES"][tval > mval])
