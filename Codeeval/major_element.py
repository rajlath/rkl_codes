from collections import Counter
cef = open("major_element.txt", "r")
for line in cef:
	elem   = [int(x) for x in line.strip().split(",")]	
	elemC = Counter(elem)
	found = None
	for k in elemC:
		if elemC[k] > len(elem)//2:
			found = k
	print(found)		
	


