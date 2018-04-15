s = input()
n = len(s)
res = 0

for i in range(n):
	depth1, depth2 = 0, 0
	for c in s[i:]:
		if c == '(':
			depth1 += 1
			depth2 += 1
		elif c == ')':
			depth1 -= 1
			depth2 -= 1
		else:
			depth1 += 1
			depth2 -= 1
		if depth1 < 0:
			break
		depth2 = max(depth2, 0)
		if depth1&1 == 0 and depth2 == 0:
			res += 1

print(res)