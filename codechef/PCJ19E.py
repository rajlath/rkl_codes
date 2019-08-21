def solve(arr, sx, sy, ex, ey):
    if sx > ex or sy > ey:return False
    if arr[sx][sy] % 2 != 0: return False
    if sx == ex and sy == ey:return True
    return solve(arr, sx + 1, sy, ex, ey) or solve(arr, sx, sy + 1, ex, ey)

n = int(input())
l = [[int(x) for x in input().split()] for _ in range(n)]
if solve(l, 0, 0, n-1, n-1):
    print("YES")
else:
    print("NO")