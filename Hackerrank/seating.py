def solve(n, m):

    if n ==0 or m == 0:return 0
    elif n%2==0 and m%2==0:
        return solve(n//2, m//2)
    elif n%2==0 and m%2==1:
        return (n + solve(n//2, m//2))
    elif n%2==1 and m%2==0:
        return (m + solve(n//2, m//2))
    else:
        return (n + m - 1 + solve(n//2, m//2))

for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    print(solve(n,m))