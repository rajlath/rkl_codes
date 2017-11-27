'''
SAMPLE INPUT
3
00010110 3
11111 4
01010 4
SAMPLE OUTPUT
3
0
-1
'''
for i in range(int(input())):
    strs, k = input().split()
    k  = int(k)
    strs = list(strs)
    lens = len(strs)
    flips = 0
    for j in range(lens - k + 1):
        if strs[j] == "0":
            for l in range(j, j+k ):
                strs[l] = ["0","1"][strs[l]=="0"]
            flips += 1
    if strs.count("0") > 0:
        print("-1")
    else:
        print(flips)


