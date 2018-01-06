def DP(a):
    dp = [0] * (len(a)+5)
    dp[0] = 1
    changed_once = False
    i = 1
    while i < len(a):
        if a[i] > a[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            if not changed_once :
                last_indx = i
                dp[i] = dp[i - 1] + 1
                changed_once = True
            else:
                i = last_indx
                dp[i] = 1
                changed_once = False
        print(dp)
        i+= 1
    return max(dp)

'''
2

6

10 2 3 1 6 7

3

3 2 3
'''
for _ in range(int(input())):
    nos = int(input())
    arr = [int(x) for x in input().split()]
    print(DP(arr))



