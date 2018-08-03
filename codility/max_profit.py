def solution(A):
    lens = len(A)

    if lens < 2:return 0

    max_profit_here = A[lens-1]
    max_profit      = 0

    for i in range(lens-2, -1, -1):
        max_profit = max(max_profit, max_profit_here - A[i])
        max_profit_here = max(max_profit_here, A[i])
    return max_profit

print(solution([23171,21011,21123,21366, 21013, 21367]))




