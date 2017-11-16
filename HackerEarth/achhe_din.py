from collections import Counter
for _ in range(int(input())):
    _ = int(input())
    arr = Counter([int(x) for x in input().split()])
    
    for i in arr:
        if arr[i] == 1:
            print(i)
