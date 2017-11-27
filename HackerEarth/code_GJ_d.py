'''
2
4
4 2 1 3
5
2 3 9 8 4
'''
updated_sum = 0
last_sum    = 0
for i in range(int(input())):
	noe = int(input())
	arr = sorted([int(x) for x in input().split()],reverse=True)
	if noe == 1:
		print(arr[0])
	else:
		last_sum = arr[0]+arr[1]
		updated_sum = last_sum
		for x in range(2,noe):
			last_sum += arr[x]
			updated_sum += last_sum		
		print(updated_sum)
		
		 
	
	

