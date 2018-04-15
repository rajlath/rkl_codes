n = int(input())
arr = [int(x) for x in input().split()]
bins = {}
ans  = 0
odds = 0
even = 0
for i in arr:
	odds += (i & 1)
	even += (i & 1) ^ 1
	print(odds, even)
	diff = odds - even
	bins[diff]= bins.get(diff, 0)
	ans += bins[diff]
	bins[diff]+= 1
print(ans)



