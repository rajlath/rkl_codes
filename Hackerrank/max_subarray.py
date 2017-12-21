'''
Sample Input 0

2
4
1 2 3 4
6
2 -1 2 3 4 -5
Sample Output 0

10 10
10 11
'''
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    currentMax = 0
    maxElement = max(arr)
    sum_pos = sum(x for x in arr if x > 0)
    current = 0
    max_arr = max(arr)

    for i in arr:
        current += i
        if current < 0:current = 0
        if current > currentMax:
            currentMax = current

    print(currentMax, sum_pos)

