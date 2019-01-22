len_A, len_B = [int(x) for x in input().split()]
m,n = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
if A[m - 1] < B[-n]:
    print("YES")
else:
    print("NO")