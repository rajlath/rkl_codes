import sys
def comb_sort(arr):
	ln = len(arr)
	gap= ln
	revisions = 0
	swapped = True
	
	while gap != 1 or swapped == True:
		
		gap = int((gap / 1.25))
		if gap < 1:
			 gap = 1
		revisions += 1
		
		swapped = False
		
		for i in range(0, ln-gap):
			if arr[i] > arr[i + gap]:
				arr[i], arr[i + gap]=arr[i + gap], arr[i]
				swapped = True
				
				
	return revisions -1
        
with open(input(), "r") as cef:
	for lines in cef:
		line = map(int,lines.strip().split(" "))			
		print(comb_sort(line))
	        
        
        
        
               
			
			
			
		
