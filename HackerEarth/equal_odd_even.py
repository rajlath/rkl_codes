'''
2 4 16 -4 5 5
'''
arr = [int(x) for x in input().split()]
a = 1
for i in range(len(arr)):
    a *= arr[i]
    print(a)



