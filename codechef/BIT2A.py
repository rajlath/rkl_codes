'''
for _ in range(int(input())):
    lens = int(input())
    vals = [int(x) for x in input().split()]
    anss = []
    for i in range(lens):
        cnts = sum([vals[j] > vals[i] for j in range(i+1, lens)])
        anss.append(cnts)
    print(*anss)
'''

#solution 2
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * n
    for i in range(n - 2, -1, -1):
        if a[i] == a[i + 1]:
            dp[i] = dp[i + 1]
        else:
            dp[i] = n - 1 - i
    print(*dp)