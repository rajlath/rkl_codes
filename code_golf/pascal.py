A=[1]
for i in range(20):
    B=[sum(A[j:j+2])for j in range(i)];B[:0],B[i+1:]=[1],[1];print(*A);A=B