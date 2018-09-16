import math
for _ in range(int(input())):
    n, a, b = [int(x) for x in input().split()]
    if a == b:
        print(n * (a * a))
    else:
        '''
        maxs = max(a*(n * n), b*(n*n))
        mins = min(a, b) * (n * n)
        for i in range(n):
            mins = min(mins, a*pow(i,2)+b*pow(n-i,2))
        print(mins)
        '''

        r1 = ((n * b) / (a + b))
        if math.ceil(r1) -  r1 <= r1 - math.floor(r1):
            r1 = math.ceil(r1)
        else:
            r1 = math.floor(r1)
        ans = r1*r1*a + (n-r1)*(n-r1)*b
        print(ans)
'''
t = int(raw_input())

for ___ in xrange(t):
	n,a,b = map(int, raw_input().split())

	r1 = b * n / (a + b)

	ans = 10101010101010101010
	for x in xrange(r1-10,r1+10):
		if 0 <= x <= n:
			ans = min(ans, x*x*a + (n-x)*(n-x)*b)
	print ans
'''








