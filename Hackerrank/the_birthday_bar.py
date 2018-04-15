import sys

def solve(n, s, d, m):
    # Complete this function
    cnt = 0
    for i in range(n-m):
        if sum(s[i:i+m]) == d: cnt += 1
    return cnt

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

'''
Sample Input 0
5
1 2 1 3 2
3 2
Sample Output 0
2
Sample Input 1
6
1 1 1 1 1 1
3 2
Sample Output 1
0
'''
