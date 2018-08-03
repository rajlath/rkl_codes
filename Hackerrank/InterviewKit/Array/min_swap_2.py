'''
Sample Input 0

4
4 3 1 2
Sample Output 0

3
'''
#This answer times out
'''
noe = int(input())
arr = [int(x) for x in input().split()]
swaps = 0
for i in range(noe):
    if arr[i] != (i + 1):
        t = i
        while arr[t] != (i + 1):
            t += 1
        arr[i], arr[t] = arr[t], arr[i]
        swaps += 1
print(swaps)
'''
#AC
def find_loops(arr, i, visited):
    loop_count = 0
    while not visited[i]:
        visited[i] = True
        i = arr[i] - 1
        loop_count += 1
    return loop_count
noe = int(input())
arr = [int(x) for x in input().split()]
visited = [False] * noe
swaps = 0
for i in range(noe):
    if not visited[i]:
        swaps += find_loops(arr, i, visited) - 1
print(swaps)


