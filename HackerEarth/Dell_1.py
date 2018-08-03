'''
Sample Input
1
5
1 2 3 2 1
Sample Output
3
'''
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    left = arr[0]
    rite = sum(arr) - left
    mins = abs(rite - left)
    for i in range(1, noe-1):
        left += arr[i]
        rite -= arr[i]
        print(left, rite)
        mins = min(mins, abs(left - rite))
print(mins)