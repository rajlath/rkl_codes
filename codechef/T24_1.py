t=int(input())
m=1000000007
for i in range(t):
	a=input()
	b=a.split()
	n=int(b[0])
	k=int(b[1])
	if (k==1):
		print (1)
	else:
		f=pow(k-1,m-2,m)
		ans=((k%m)*((pow(k,n,m)-1)%m)*(f%m))


		print (ans%m)
