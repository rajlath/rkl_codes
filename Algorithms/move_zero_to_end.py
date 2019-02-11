A = [7,0,0,3,0,2,3,3,6,3]
"""
ans = []
cnt = 0
for i in A:
    if i != 0:
        cnt += 1
        ans.append(i)
ans += [0]*cnt
print(ans)
"""
i = j = 0
while i < len(A):
    if A[i] != 0:
        A[j] = A[i]
        j += 1
    i += 1
while j < len(A):
    A[j] = 0
    j += 1
print(A)


