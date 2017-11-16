import sys

def swap(arr, lo, hi):
	i, j, pivot = lo, hi, arr[lo]
	while True:
		while arr[i] < pivot:
			i += 1
		while arr[j] > pivot:
			j -= 1
		if i >= j:
			return j
		arr[i], arr[j] = arr[j], arr[i]

def count_pivots(arr, lo, hi):
	global pivots
	if lo < hi:
		swapped = swap(arr, lo, hi)
		pivots += 1		
		count_pivots(arr, lo, swapped-1)
		count_pivots(arr, swapped+1, hi)
		
	

pivots = 0
with open(input(), "r") as cef:
	for lines in cef:
		arr = list(map(int, lines.strip().split()))		
		count_pivots(arr, 0, len(arr)-1)
		print(pivots)
		pivots = 0
