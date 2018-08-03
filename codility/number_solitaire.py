# https://codility.com/programmers/lessons/17-dynamic_programming/

# python 3.6.0

def solution(A):
    '''
    type A: int array
    rtype : int
    '''
    max_here = [0] * len(A)
    max_here[0] = A[0]
    for i in range(1, len(A)):
        
        if i <= 6:
            max_here[i] = A[i] + max(max_here[0:i])
        else:
            max_here[i] = A[i] + max(max_here[i - 6: i])
    return max_here[-1]

print(solution([1,-2,0,9,-1,-2]))



