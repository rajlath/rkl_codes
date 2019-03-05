nb_test = int(input())
for _ in range(nb_test):
	nb_elem = int(input())
	elemes  = [int(x) for x in input().split()]
	best_here = 0
	best_alls = 0
	for i in elemes:
		best_here += i
		if best_here < 0: best_here = 0
		best_alls = max(best_alls, best_here)
	print(best_alls)

