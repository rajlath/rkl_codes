def solution(S):
    stack = []
    if len(S) == 0:
        return 1
    for i in S:
        if i == "("    :
            stack.append(i)
        else:
            if len(stack) <=0:
                return 0
            stack.pop()
    if len(stack)==0:return 1
    else:return 0

print(solution("())"))