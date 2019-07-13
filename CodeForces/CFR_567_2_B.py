n = int(input())
s = input()
ans = int(s)
for i in range(-1, 2):
	mid = n // 2 + i
	while (mid > 0 and mid < n and s[mid] == '0'):
		if i < 0:
			mid -= 1
		else:
			mid += 1
	if mid > 0 and mid < n:
		ans = min(ans, int(s[:mid]) + int(s[mid:]))

print(ans)
