N = int(2e5) + 5
b = [0] * (2 * N)
def solve(arr, n, k):
    curr = N
    ok   = 0
    ret  = 0
    b[curr] += 1
    for i in range(n):
        if arr[i] <= k:
            curr += 1
            ok += b[curr]
        else:

            ok -= b[curr]
            curr -= 1


        ret += ok
        b[curr] += 1
        print(ret, curr, b[curr], ok)
    return ret
n, m = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
print(solve(arr,n, m) - solve(arr, n,  m-1))