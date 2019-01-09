n, m, k = [int(x) for x in input().strip().split()]
elems   = [int(x) for x in input().split()]
elem = [x for x in  elems if pow(x,m,k) == 0]
print(len(elem))