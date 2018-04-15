def solution(A):
    # write your code in Python 3.6
    sums = sum(A)
    left = 0
    rite = sums
    min_diff = int(10e7)
    for i in range(len(A)):
        left = left + A[i]
        rite = rite - A[i]
        curr_diff = max(left, rite)- min(left, rite)
        print(left, rite, curr_diff)
        min_diff = min(curr_diff, min_diff)
    return min_diff

print(solution([3, 0]))

