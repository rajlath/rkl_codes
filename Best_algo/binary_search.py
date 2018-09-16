from seq import create_seq

seq = list(create_seq(1, 10, 20))

def binary_search_rec(s, v):
    '''
    search and return index of v in s if v is available else return -1
    '''
    if not s: return None
    mid = len(s) // 2
    print(mid, s[:mid], s[mid+1:])
    if v ==  s[mid]: return mid
    elif v < s[mid]: return binary_search_rec(s[:mid], v)
    else:             return binary_search_rec(s[mid+1:], v)

def binary_search_itr(s, key):
    hi, lo = len(s), 0
    while lo < hi:
        mid = (hi + lo) // 2
        if key == s[mid]: return mid
        elif key < s[mid]:hi = mid
        else: lo = mid + 1
    return -1




print(seq)
seq = [1,2,5,7,10,12,12,14,15,42,64,90]
print(binary_search_itr(seq, 14))
print(binary_search_rec(seq, 14))

