def merge_sort(A):
    if len(A) > 1:
        mid = len(A)//2
        left= A[:mid]
        rite= A[mid:]
        merge_sort(left)
        merge_sort(rite)
        i = j= k = 0
        while i < len(left) and j < len(rite):
            if left[i] < rite[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = rite[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(rite):
            A[k] = rite[j]
            j += 1
            k += 1
        print('merging ', A )
        return(A)

merge_sort([355, 97, 846, 215])
