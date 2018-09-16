def merge(arr1, arr2):
    inv = 0
    res = []
    while len(arr1)>0 and len(arr2)>0:
        if arr1[0] <= arr2[0]:
            res.append(arr2.pop(0))
        else:
            inv += len(arr1)
            res.append(arr1.pop(0))
    if len(arr1) == 0: res += arr2
    if len(arr2) == 0: res += arr1
    return res, inv


def sort(arr):
    lens = len(arr)
    mid = lens // 2
    if lens >=2:
        sorted1, count1 = sort(arr[:mid])
        sorted2, count2 = sort(arr[mid:])
        result, counts  = merge(sorted1, sorted2)
        #print(sorted1, sorted2)
        return result, counts + count1 + count2
    else:
        return arr, 0

def count_inversion(arr):
    sarr, inv = sort(arr)
    return inv


for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    print(count_inversion(a))