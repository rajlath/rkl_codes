'''
4
1 3 2 3

2
2 2
'''
noe  = int(input())
ele  = [int(x) for x in input().split()]
eles = sorted(ele)
min_odd = None
for i in range(noe):
	if eles[i]%2==1:
		min_odd = eles[i]
		break
		
if sum(ele) % 2 == 0:
	if min_odd != None:
		print("First")
	else:
		print("Second")	
else:
	print("First")		
	
