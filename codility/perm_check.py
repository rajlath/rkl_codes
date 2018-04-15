def solution(A):
    # write your code in Python 3.6
    n = len(A)
    arr = [0] * (n + 1)

    for x in A:
        if x < 1 or x > n:
            return 0
        arr[x - 1] +=1

    for i in range(n):
        if arr[i] != 1:
            return 0
    return 1



print(solution([4,1,3,2]))