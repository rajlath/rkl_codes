from collections import Counter
def solution(A):
    # write your code in Python 3.6
    x = 0
    for i in A:
        x^=i
    return x


print(solution([1, 2,3, 4, 3, 1, 2, 4, 4]))