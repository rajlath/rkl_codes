import sys

def cocktail(arr, n):
	todo = min(n, len(arr)//2)
	for i in range(todo):
		for j in range(i+1, len(arr)-i):
			if arr[j-1] > arr[j]:
				arr[j-1], arr[j] = arr[j], arr[j-1]
		for j in range(len(arr)-1-i, i, -1)		:
			if arr[j-1] > arr[j]:
				arr[j-1], arr[j] = arr[j], arr[j-1]
	return arr			
				
			
	


with open(input(), "r") as cef:
	for lines in cef:
		lines = lines.strip().split("|")
		steps = int(lines[1].strip() )
		arr  = list(map(int, lines[0].strip().split()))
		arrs = cocktail(arr, steps)
		print(" ".join(map(str,arrs)))
		
