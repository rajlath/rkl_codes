
import sys





def solve(beads, pos):
	if len(beads) == pos:
		return 1 if 1 + beads[- 1] in prime_list else 0
	result = 0
	if beads[pos] + beads[pos-1] in prime_list:
		result += solve(beads, pos + 1)
	for i in range(pos+2, len(beads), 2):
		if beads[pos-1] + beads[i] in prime_list:
			beads[i], beads[pos] = beads[pos], beads[i]
			result += solve(beads, pos + 1)
			beads[i], beads[pos] = beads[pos], beads[i]
	return result
    
    
prime_list = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}    
with open(input(),"r") as cef:
	for lines in cef:
		numBead = int(lines)
		print(solve(list(range(1, numBead + 1)), 1))
		
    

