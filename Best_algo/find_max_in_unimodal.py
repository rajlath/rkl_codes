'''
unimodal means elements has an increasing and then decreasing elements
'''
seq = [1, 2, 5, 6, 7, 10, 12, 9, 8, 7, 6]

def find_max_in_unimodal(seq):
    if len(seq) <= 2: return None
    left = 0
    rite = len(seq) - 1
    while rite > left + 1:
        mid = (left + rite)//2
        if seq[mid] > seq[mid-1] and seq[mid] > seq[mid+1]:
            return seq[mid]
        elif seq[mid] > seq[mid-1] and seq[mid] < seq[mid+1]:
            left = mid
        else:
            rite = mid
    return None
print(find_max_in_unimodal(seq))


