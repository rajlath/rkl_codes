'''
example, given:
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5
'''
def solution(A):
    # write your code in Python 3.6
    lens = len(A)
    to_west = 0
    passing_by = 0
    AR = A[::-1]
    for i in range(lens-1, -1, -1):
        if A[i] == 0:
            passing_by += to_west
            if passing_by > 1000000000:
                return -1
        else:
            to_west += 1
    return passing_by

print(solution([0,1,0,1,1]))


