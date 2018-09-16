#approach sliding window
def solve(arr):
    n = len(arr)
    visited = {x:0 for x in range(n)}
    right = 0
    left  = 0
    while right < n:
        while right < n and not visited[arr[right]]:
            visited[arr[right]] = True
            right += 1
        print(*arr[left:right])
        while right < n and visited[arr[right]]:
            visited[arr[left]] = False
            left += 1

arr = [5,2,3, 5,4, 3]
print(solve(arr))