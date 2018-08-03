def solution(A):
    lens = len(A)
    maybe = -1
    maybe_cnt = 0
    maybe_idx = -1
    for i in range(lens):
        if maybe_cnt == 0:
            maybe = A[i]
            maybe_cnt += 1
            maybe_idx = i
        else:
            if A[i] == maybe:
                maybe_cnt += 1
            else:
                maybe_cnt -= 1
    if A.count(maybe) <= lens//2:return -1
    return maybe_idx

print(solution([3,4,3,2,3,-1,3, 3]))
