a,b,c,n=map(int,input().split())
x=n-(a+b-c)
if(x>0 and a>=c and b>=c):
	print(x)
else:
	print(-1)
