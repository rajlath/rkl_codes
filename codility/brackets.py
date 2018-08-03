'''
def solution(S):
    if len(S) % 2 == 1:   return 0

    matched = {"]":"[", "}":"{", ")": "("}
    to_push = ["[", "{", "("]
    stack = []

    for element in S:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif matched[element] != stack.pop():
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0

'''
def solution(S):
    stack = []
    ans   = 1
    ins   = '([{'
    out   = ')]}'
    if len(S)%2 != 0:return 0
    for s in S:
        if s in ins:
            stack.append(s)
        else:
            if len(stack)==0 or ins[out.index(s)] != stack.pop():
                return 0

    if len(stack) == 0:ans = 1

    return ans
'''
def solution(S):
    stack = []
    ans   = 1
    ins   = '([{'
    out   = ')]}'
    for s in S:
        if s in ins:
            stack.append(s)
        else:
            if stack[-1] != ins[out.index(s)]:
                ans = 0
                break
            else:
                stack.pop()
    if len(stack) > 0:ans = 0

    return ans
'''
print(solution( "([)()]" ))
