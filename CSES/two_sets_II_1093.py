MOD = 1000000007

def solve(i, s):
	global n, t, sums, c
	if i == n:
		return s == t
	if c[i][s] != -1:return c[i][s]
	k = solve(i + 1, s)
	if (s + i <= t):k += solve(i + 1, s + i)
	k %= MOD
	c[i][s] = k
	return k

n = int(input())
t = (n * (n + 1)) // 2
if t % 2 == 1:
	print("0")
else:
	t //= 2
	c = [[-1 for x in range(250001)] for y in range(501)]
	ans = solve(1, 0)
	if ans < 0:ans += MOD
	print(ans)
