'''
ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans
'''
for _ in range(int(input())):
    ast = [int(x) for x in input().split()]
    stack = []
    ans = []
    for this in ast:
        if this > 0:
            stack.append(this)
        else:
            killed = False
            while stack:
                if abs(this) < stack[-1]:
                    killed = True
                    break
                elif -this == stack[-1]:
                    killed = True
                    stack.pop()
                    break
                else:
                    stack.pop()
            if not killed:
                ans.append(this)
    ans.extend(stack)
    if len(ans)==0:
        print("NOTHING")
    else:
        print(*ans)