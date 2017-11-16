noe, nop, nfe = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
fav = [int(x) for x in input().split()]
sums = sum(arr)
for i in range(nop):
	l, r, k = [int(x) for x in input().split()]	
	arr = [a + k if (a not in fav) and a in arr[l-1:r] else a for a in arr]
	print(arr)
	print(sum(arr))
	
	
