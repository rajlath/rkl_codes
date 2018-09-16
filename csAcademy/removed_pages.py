def mypop(arr, x):
    try:
        a = arr.index(x)
        del arr[a]
        return (1, arr)
    except ValueError:
        return (0, arr)



nop = int(input())
arr = [int(x) for x in input().split()]
cnt = 0
while arr:
    x = arr.pop(0)
    if x % 2 :
        y = x + 1
    else:
        y = x - 1
    res, arr = mypop(arr, y)
    #print(res, arr, x, y)
    cnt += res
print(nop - cnt)
