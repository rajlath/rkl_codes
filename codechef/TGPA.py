
'''
Sample Input:
1
3
3 4 5
5 7 11

Sample Output:
368
'''
for _ in range(int(input())):
    nop = int(input())
    intervals = [int(x) for x in input().split()]
    last_time = [int(x) for x in input().split()]
    may_be = last_time[-1]
    while True:
        may_be += intervals[-1]
        print(may_be)
        failed=False
        for i in range(nop-1):
            if (may_be - last_time[i])%intervals[i]!= 0:
                failed=True
                break
        if failed:continue
    print(may_be)