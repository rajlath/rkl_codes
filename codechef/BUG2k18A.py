for _ in range(int(input())):
	nots,cst = [int(x) for x in input().split()]
	costs = [int(x) for x in input().split()]
	yz = len(list(filter(lambda x: x<=cst,costs)))
	print(nots,yz,yz)
