n, m = [int(x) for x in input().split()]
arr  = [int(x) for x in input().split()]
#arrs = sorted(arr, reverse=True)
sum_here = 0
for i in range(n):
    sum_here += arr[i]
    j = p =  0
    sh = sum_here
    el = sorted(arr[:i], reverse=True)
    #print(el, sorted(arr, reverse=True)[:i])
    while sh > m:
        sh -= el[j]
        p += 1
        j += 1
    print(p, end=' ')
