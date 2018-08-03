n, k = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
arr1 = [arr[0]]
for i in range(1, n-1):
    arr1.append(arr1[-1] + k)

print(len(set(arr) - set(arr1)))