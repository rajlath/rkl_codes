def solution(A):
    # write your code in Python 3.6
    sums = ((len(A)+ 2) * (len(A)+1)) // 2
    for i in A:
        sums -= i
    return sums






print(solution([1,3,2,5]))