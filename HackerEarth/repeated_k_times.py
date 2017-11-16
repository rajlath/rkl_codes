'''
10
1 1 2 2 2 2 3 3 4 4
4

1 2
'''
from collections import Counter
sl  = input()
arr = Counter([int(x) for x in input().split()])
k = int(input())
maybe = []
for x in arr:
    if arr[x] == k:
        maybe.append(x)
       
print(min(maybe))        


    
