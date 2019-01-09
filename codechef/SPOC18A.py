t = int(input())
o = []
for i in range(t):
	n = list(map(int, input().split()))
	ans = -1
	for num in range(n[0],n[1]+1):
		if num%n[0] == 0 and n[1]%num == 0:
			ans = num
			break
	print(ans)