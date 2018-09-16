s = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]

def quick_sort(seq):
    if len(seq) < 2: return seq
    mid = len(seq)//2
    piv = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [ x for x in seq if x <= piv]
    hi = [ x for x in seq if x >  piv]
    return quick_sort(lo) + [piv] + quick_sort(hi)

print(quick_sort(s))