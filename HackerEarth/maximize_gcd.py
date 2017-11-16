from fractions import gcd
from functools import reduce
a = 5
arr = [4, 8, 6, 9, 3]

max_gcd   = 0
max_size  = 0


for i in range(1, a):
	curr_gcd = reduce(gcd, (arr[i:]))
	
	if curr_gcd > max_gcd:
		max_gcd = curr_gcd
		max_size= i
		
		
print(max_size)		
	
