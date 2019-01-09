x = int(input())
ans = [-1]
for i in range(x-1, 1, -1):
    done = False
    for j in range(i-1, 1, -1):
        if i % j == 0:
            ans = [i, j]
            done = True
            break
    if done:break
print(*ans)

