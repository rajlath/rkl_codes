x, k = map(int, input().split())
mod = 10 ** 9 + 7
ans = pow(2, k, mod) * (2 * x - 1) + 1
print(ans % mod if x else 0)