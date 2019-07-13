import sys
import itertools
import math
def maximumGcdAndSum(A, B):
    C = []
    C.append(A)
    C.append(B)
    print(*C)
    D=[]
    E=[]
    gcds=[1]
    sums=[]
    prodC = itertools.product(*C)
    for element in prodC:
        gcdVal = math.gcd(element[0],element[1])
        D.append((gcdVal,sum(element)))
        gcds.append(gcdVal)
    # sums.append(sum(element))
# print(D)
    maxGCD = max(gcds)
    sumsL = [1]
#print(gcds)
# print(sums)
    for i in D:
        if i[0] == maxGCD:
            sumsL.append(i[1])
    return max(sumsL)

print(maximumGcdAndSum([4,4,6],[7]))