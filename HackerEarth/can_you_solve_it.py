for _ in range(int(input())):
    _ = input()
    arr = [int(x) for x in input().split()]
    arr1 = []
    arr2 = []
    for i, v in enumerate(arr):
        arr1.append(i + v)
        arr2.append(v - i)
    print(max((max(arr1) - min(arr1), max(arr2) - min(arr2))))    
