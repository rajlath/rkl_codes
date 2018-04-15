'''
3
2
1321 2450
3
500 123 873
4
600 800 150 700

2450
1496
2400
'''
for _ in range(int(input())):
    nos = int(input())
    arr = [int(x) for x in input().split()]
    if nos == 2:
        print(max(arr))
    else:
        print(sum(arr) - min(arr) + min(arr)*(nos// 2 + nos%2))

