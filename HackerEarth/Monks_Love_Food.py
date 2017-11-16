stack = []
noq = int(input())
for _ in range(noq):
    ar = [int(x) for x  in input().split()]
    if ar[0] == 1:
        if len(stack) < 1:
            print("No Food")
        else:
            print(stack[-1])
            stack = stack[:-1]
    else:
        stack.append(ar[1])
