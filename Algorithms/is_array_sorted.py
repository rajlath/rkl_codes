def is_array_sorted(A):
    if len(A) == 1:return True
    return A[0] <= A[1] and is_array_sorted(A[1:])

A= [220, 246, 277, 321, 454, 534, 565,2345,9331]
print(is_array_sorted(A))
