def find_smaller(arr, n):
    results = [0]*len(arr)
    results[n-1] = 0
    for i in range(n-2, -1, -1):
        for j in range(i+1, n, 1):
            if arr[i] > arr[j]:
                results[i] += 1
    return results

noe = int(input())
arr = [int(x) for x in input().split()]
ans = find_smaller(arr, noe)
print(" ".join(map(str, ans)))


