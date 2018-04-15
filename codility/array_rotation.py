def solution(A, K):
    # write your code in Python 3.6
    if len(A) = 0:
        return []
    for i in range(K):
        A = [A[-1]]+A[:-1]
    return(A)

solution([1,2,3,4], 4)