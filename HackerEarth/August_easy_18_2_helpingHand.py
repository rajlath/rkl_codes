a = [2,1,4,6,3]

n,m=list(map(int,input().strip().split()))
A=list(map(int,input().strip().split()))

def helpingHand(A):
    B=[A[0]] + [0]*(len(A)-1)
    for i in range(1,len(B)):
        B[i]=A[i-1]|A[i]
    return B

for i in range(m):
    B=helpingHand(A)

    if B!=A:
        A=B
    else:
        break
print(*A)