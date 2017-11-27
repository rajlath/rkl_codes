#!/bin/python

import sys

def surfaceArea(A, h, w):

    res = h * w * 2
    for i in range(h):

        res += A[i][0]
        res += A[i][-1]
        for j in range(w - 1):
            res += abs(A[i][j] - A[i][j + 1])

    for j in range(w):
        res += A[0][j]
        res += A[-1][j]
        for i in range(h - 1):
            res += abs(A[i][j] - A[i+1][j])
    return res

    # Complete this function

if __name__ == "__main__":

    H, W = [int(x) for x in input().split()]
    A = []
    for A_i in range(H):
        A_temp = list(map(int,input().strip().split(' ')))
        A.append(A_temp)
    print(A)
    result = surfaceArea(A, H, W)
    print(result)

    #!/bin/python3

import sys

def surfaceArea(A):
    # Complete this function
    ans = 0
    #print(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                nx = j + dx
                ny = i + dy
                if 0 <= nx < len(A[0]) and 0<= ny < len(A):
                    if nx >= j and ny >= i:
                        #print(ny, nx)
                        ans += abs(A[i][j] - A[ny][nx])
                else:
                    ans += A[i][j]

    return ans

if __name__ == "__main__":
    H, W = input().strip().split(' ')
    H, W = [int(H), int(W)]
    A = []
    for A_i in range(H):
        A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
        A.append(A_t)
    result = surfaceArea(A)
    print(result + H*W + H*W) 