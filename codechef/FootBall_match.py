t=int(input())
while t>0:
	n=int(input())
	if n>0:
		a=input()
		aas=1
		bs=0
		for i in range(n-1):
			b=input()
			if a==b:
				aas+=1
			else:
				c=b
				bs+=1
		if aas==bs:
			print("Draw")
		else:
			if aas>bs:
				print(a)
			else:
				print(c)
	else:
		print("Draw")
	t-=1