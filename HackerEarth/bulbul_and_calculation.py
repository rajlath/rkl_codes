'''
3
4
13 6 12 19
25
5
4 1 16 15 2
17
8
1 16 2 15 4 12 2 5
23
'''
for _ in range(int(input())):
    nos = int(input())
    nums = [int(x) for x in input().split()]
    target = int(input())

    def twoSum(nums, target):
        d={}
        for i,num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num]=i
        return [-1]

    print(*twoSum(nums, target))






