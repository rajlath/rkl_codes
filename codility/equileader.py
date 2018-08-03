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
    if A.count(maybe) <= lens//2:return 0
    else:
        leader = maybe
    total_leaders = sum([1 for x in A if x == leader] )
    leaders_till_now = 0
    equileader = 0
    for i in range(len(A)):
        if A[i] == leader:leaders_till_now += 1
        if leaders_till_now > (i+1)//2 and total_leaders - leaders_till_now >= (len(A) - i + 1 )//2:
            equileader += 1
    return equileader



print(solution([4,3,4,4,4,2]))
