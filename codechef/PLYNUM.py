'''
Given two non-zero intgers A and B
reach B from A using following operations
1. Deduct 1 from A
2. Add 3 to A
3. Multiply A with 2
These operation can be performed as many time as required.
However solution should be minimum number of operation required
Constraints:
T Number of testcases 1<= T <= 100
A B start intger and end integer 0 <= A, B <= 2 * 10 ** 3
Sample
Input
2
4 7
0 10
Output
1          # 4 + 3
4          # 0->3->6->5->10
'''
#https://www.codechef.com/ENAU2018/problems/PLYNUM
#oorja oorja.halt@gmail.com
#13 08 2018
#python 3.6

def get_ops_count(a, b):
    if a == b : return 0
    dp = [-1] * 2001
    dp[a] = 0
    cache = [a]
    while cache:
        cur = cache.pop(0)
        if cur == b: return dp[cur]
        for m in [cur-1, cur+3,cur*2]:
            if m > 0 and m < 2001 and dp[m] is -1:
                dp[m] = dp[cur] + 1
                cache.append(m)


for _ in range(int(input())):
    a, b =[int(x) for x in input().split()]
    print(get_ops_count(a, b))

