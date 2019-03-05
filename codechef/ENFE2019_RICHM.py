nb_test = int(input())
for _ in range(nb_test):
	a,b = [int(x) for x in input().split()]
	if b == 0:
		print("cannot distribute")
	else:
		divs= a // b
		if divs > 0:
			print(divs)
		else:
			print("cannot distribute")
