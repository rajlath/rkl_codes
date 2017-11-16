'''
7
1 5 7 5 6 7 5
5
1 2
2 3
4 6
1 7
3 6
'''
n = int(input())
a = [int(x) for x in input().split()]
sums = sum(a)
has = [0]*(n+1)
j = 0
for i in range(n):
	tmp = sums -a[0]
	if i != 0 and  	i+1 != n:
		if tmp%3==0 and a[i-1]+a[n-1]==10:j+=1
		else:
			if i == 0:
				if tmp%3==0 and a[n-1]==0:j+=1
			else:
				if tmp%3==0 and a[i-1]==0: j+=1
	print(j)			
	has[i+1]=j
print(has)		 
for _  in range(int(input())):
	l,r = [int(x) for x in input().split()]
	print(has[r]-has[l-1])  			
                    
			
