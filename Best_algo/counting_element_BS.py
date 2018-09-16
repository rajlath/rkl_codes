seq = [1,2,2,2,2,2,2,5,6,6,7,8,9]
k   = 2

def binary_search(seq, v):
    if len(seq) <= 2: return None
    lo = 0
    hi = len(seq) - 1
    while lo <= hi:
        mid = (hi + lo)//2
        if seq[mid] == v : return mid
        if v < seq[mid]: hi = mid
        else:lo = mid + 1
    return None

def count_element(seq, k):
    indx = binary_search(seq, k)
    #print(indx)
    cnt  = 0
    #if indx == len(seq) - 1: return 1
    for i in range(indx, len(seq)):
        if seq[i] == k:
            cnt += 1
        else:
            break
    for i in range(indx-1, -1, -1):
        if seq[i] == k:cnt += 1
        else:break

    return cnt

print(count_element(seq, 6))

