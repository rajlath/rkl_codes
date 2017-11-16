
'''lst = [1, 4, 6, 7, 9, 3, 2]

for scanIndex in range(len(lst)):
	
	minIndex = scanIndex
	for restIndex in range(scanIndex+1, len(lst)):
		if lst[restIndex] < lst[minIndex]:
			minIndex = restIndex
		if minIndex != restIndex:
			lst[minIndex], lst[restIndex] = lst[restIndex], lst[minIndex]
		print(lst)		
			
print(lst)'''
from bintrees import BinaryTree
data={3:'White',2:'Red',1:'Green',5:'Orange',
4:'Yellow',7:'Purple',0:'Magenta'}
tree = BinaryTree(data)
print(tree)

import heapq
heap = []
data={3:'White',2:'Red',1:'Green',5:'Orange',
4:'Yellow',7:'Purple',0:'Magenta'}
for key, value in data.items():
	heapq.heappush(heap, (key, value))
heap.sort()
for item in heap:
	print("key :",item[0],'value :',item[1])	
print(heapq.nlargest(1, heap)[0][0])	







			
			
		
