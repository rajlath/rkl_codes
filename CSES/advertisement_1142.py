nb_rods = int(input())
heights = [int(x) for x in input().split()] + [0]
m = 0
stack = []
for i in range(nb_rods + 1):
    while len(stack) > 0 and heights[i] <= heights[stack[-1]] :
        h = heights[stack[-1]]
        stack.pop()
        if len(stack) > 0:
           k = stack[-1]
        else:
           k = -1
        m = max(m, (i - k - 1) * h )
    stack.append(i)
    #print(stack)

print(m)
