def solution(A):
    # write your code in Python 3.6
    N = len(A)
    arr = [0] * (N+2)
    for ele in arr:
        if 1 <= ele <= N:
            arr[ele] += 1
    for i in range(1, N+2):
        if arr[i] == 0:
            return i
    return -1


