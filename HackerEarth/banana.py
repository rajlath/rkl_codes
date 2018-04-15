def may_be(arr, np, qty):
    hours = 0
    for i in range(np):
        hrs = arr[i]//qty
        if arr[i]%qty == 0:
            hours += hrs
        else:
            hours += (hrs +1)
    return hours

for _ in range(int(input())):
    n,h = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    sums = sum(arr)
    low = 0
    high= sums
    while low < high:
        mid = (low + high) //2
        could_take = may_be(arr, n, mid)
        if could_take <= h:
            high = mid
        else:
            low  = mid + 1
    print(low)

