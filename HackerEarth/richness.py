#copied
from collections import defaultdict
 
def read_ints():
	return map(int, raw_input().split())
	
def update(N, L, R, C, P, Q, S):
	# print "Enter update"
	LL = (L * P + R) % N + 1
	RR = (R * Q + L) % N + 1
	C = (C * S) % 1000000 + 1
	if LL > RR:
		LL, RR = RR, LL
	return (LL, RR, C)
	
def solveCase():
	n, m = read_ints()
	L, R, C, P, Q, S = read_ints()
	inserts, deletes = [0] * (n + 1), [0] * (n + 1)
	for i in xrange(m):
		inserts[L] += C
		deletes[R] += C
		L, R, C = update(n, L, R, C, P, Q, S)
	
	ret = (0, 1)
	cur = 0
	for i in xrange(1, n + 1):
		cur += inserts[i]
		if cur > ret[0]:
			ret = (cur, i)
		cur -= deletes[i]
	print ret[1], ret[0]
	
def main():
	T = int(raw_input().strip())
	for t in xrange(T):
		solveCase()
		
if __name__ == '__main__':
	main()
