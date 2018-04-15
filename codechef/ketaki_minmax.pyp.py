'''
n*(n+1)*(2*n+1)/6
'''

def sol(n):
    return n*(n+1)*(2*n+1)//6

for i in range(int(input())):
    n = int(input())
    ans = sol(n) + sol(n-1)
    print(ans)