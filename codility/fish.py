def solution(A, B):
    alive = 0
    ds    = []
    ds_cnt= 0
    for i in range(len(A)):
        if B[i] == 1:
            ds.append(A[i])
            ds_cnt += 1
        else:
            while ds_cnt != 0:
                if ds[-1] < A[i]:
                    ds_cnt -= 1
                    ds.pop()
                else:
                    break
            else:
                alive += 1
    return alive + len(ds)

print(solution([4,3,2,1,5],[0,1,0,0,0]))
