def solution(A):
    min_avg_val = (A[0] + A[1]) // 2.0
    min_avg_pos = 0

    for i in range(len(A) - 2):
        cur_2_avg   = (A[i] + A[i+1]) // 2.0
        min_avg_val = min(min_avg_val, cur_2_avg)
        if min_avg_val == cur_2_avg:min_avg_pos = i

        cur_3_avg   = (A[i] + A[i+1] + A[i+2]) // 3.0
        min_avg_val = min(min_avg_val, cur_3_avg)
        if min_avg_val == cur_3_avg:min_avg_pos = i

    last_avg =  A[-1] + A[-2] // 2.0
    min_avg_val = min(min_avg_val, last_avg)
    if min_avg_val == last_avg: min_avg_pos = len(A) - 2

    return min_avg_pos

print(solution([4,2,2,5,1,5,8]))

