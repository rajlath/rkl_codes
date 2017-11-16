'''
2
5
8 8 9 5 9
5
3 3 3 5 3
'''

for _ in range(int(input())):
    input()
    arr = sorted([int(x) for x in input().split()])
    if arr.count(arr[0])%2==0:print("Unlucky")
    else:print("Lucky")
