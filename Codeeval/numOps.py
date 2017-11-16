import sys
import itertools


    
def canBe42(combs):
	for candidate in combs:
		candidate = list(candidate)
		res = [candidate.pop()]
		while candidate:
			x = candidate.pop()
			possible = []
			for vals in res:
				a, b, c = vals + x, vals - x, vals * x
				possible.append(a )   
				possible.append(b ) 
				possible.append(c ) 
			res = possible[:]
		if 42 in possible:
			return True
	return False				


with open(input(), "r") as cef:
	for lines in cef:
		operands = list(map(int, lines.split()))
		allcombs = list(itertools.permutations(operands, 5))
		print("YES" if canBe42(allcombs) else "NO")


