'''
5 2  
1 5 3 4 2  
'''

noe, k = [int(x) for x in input().split()]
arr = sorted([int(x) for x in input().split()])
pairs = 0
for i in range(noe):
    for j in range(i+1,noe):
        if arr[j] - arr[i] == k:
            pairs += 1
            break
print(pairs)        
