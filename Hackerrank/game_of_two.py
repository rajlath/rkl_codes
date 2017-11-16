"""
Sample Input 0

1
5 4 10
4 2 4 6 1
2 1 8 5
Sample Output 0

4
"""

for _ in range(int(input())):
    lenA, lenB, maxSum = [int(x) for x in input().split()]
    arrA =  [int(x) for x in input().split()]
    arrB =  [int(x) for x in input().split()]

    stkA = []
    sums = 0
    cnt = 0
    for i in range(lenA):
        sums += arrA[i]
        if sums >= maxSum:            
            cnt += 1
        else:
            break
    cnt = i
    j = 0

    while j < lenB and i > 0:
        sums += arrB[j]
        j+= 1        
        while sums > maxSum and i > 0:            
            sums -= arrA[i]
            i -= 1
            
    if sums < maxSum and i+j>cnt:
        count=i+j                   
        

    print(cnt)        
    
        
    