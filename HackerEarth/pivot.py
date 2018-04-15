'''
2
1 7 3 6 5 6
1 2 3
'''

for _ in range(int(input())):
    nums = [int(x) for x in input().split()]
    S = sum(nums)
    leftsum = 0
    ans = -1
    for i, x in enumerate(nums):
        if leftsum == (S - leftsum - x):
            ans =  i
            break
        leftsum += x
    print(ans)

