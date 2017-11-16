'''
SAMPLE INPUT 
5
1 1 2 1 3
3
1 5
2 4
3 5
SAMPLE OUTPUT 
3
2
3
'''
noe = int(input())
seen = []

arr = [0] + [int(x) for x in input().split()] + [0]

for i in range(int(input()))   :
    l, r = [int(x) for x in input().split()]
    print(len(set(arr[l:r+1])))
    

