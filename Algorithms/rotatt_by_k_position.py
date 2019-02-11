def rotate_k_position(A, k):
    return A[k:] + A[:k]

print(rotate_k_position([1,2,3,4,5,6,7,8,9,10], 6))
print(rotate_k_position("rajLath", 3))