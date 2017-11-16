visited = []
n = int(input())
for i in range(n):
    curr = input()
    if curr in visited:
        print("YES")
    else:
        visited.append(curr)
        print("NO")
