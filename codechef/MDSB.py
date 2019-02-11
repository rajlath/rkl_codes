for _ in range(int(input().strip())):
    n = int(input().strip())
    arr = "".join(list(input().strip().split())).split("0")
    arr = [len(x) for x in arr]
    maxl = 0
    for i in range(len(arr)-1):
        maxl = max(maxl, arr[i] + arr[i+1])
    print(maxl+1)