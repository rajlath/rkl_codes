def solve(m, a):
    stack = []
    x = 0
    for i in range(m + 1):
        while len(stack) > 0 and a[i] < a[stack[-1]]:
            h = a[stack[-1]]
            stack.pop()
            if len(stack) == 0:
                k = -1
            else:
                k = stack[-1]
            x = max(x, h * (i - k - 1))
        stack.append(i)
    return x



n, m = [int(x) for x in input().split()]
a = [0] * (m + 1)
for i in range(n):
    curr = [x for x in input()]
    for j in range(m):
        if curr[j] == ".": a[j] +=1
        else:a[j] = 0
print(max(0, solve(m, a)))