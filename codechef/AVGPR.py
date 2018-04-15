'''
3
2
2 2
3
2 1 3
6
4 2 5 1 3 5
'''

for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    sar = set(arr)

    cnt = 0
    for i in range(noe):
        for j in range(i+1, noe):
            if (arr[i]+arr[j])//2 in sar:cnt += 1
    if cnt == 1:
        print(cnt)
    else:
        print(cnt//2)
