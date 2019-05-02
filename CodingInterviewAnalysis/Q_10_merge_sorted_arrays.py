from random import randint
def create_random_arrays(lens, ranges, is_sorted=False, is_unique=True):
    '''
    create an array having lens number of random integer
    ranges defines number to pick from range 1, to ranges
    is_sorted when set True, returns a sorted array
    '''
    rets = []
    while len(rets) < lens:
        curr = randint(1, ranges)
        if is_unique:
            if curr in rets:continue
        rets.append(curr)
    if is_sorted:rets = sorted(rets)
    return rets

def merge_two_sorted_arrays(a, b):
    '''
    a, b are sorted integer arrays.
    return c which is created by merging a and b
    c should be sorted as well
    '''
    lena = len(a)
    lenb = len(b)
    c = [0 for _ in range(lena + lenb)]
    insert_at = len(c) - 1
    while lena and lenb:
        if a[-1] >= b[-1]:
            c[insert_at] = a.pop()
            lena -= 1
        else:
            c[insert_at] = b.pop()
            lenb -= 1
        insert_at -= 1
    if lena:
        for i in range(lena):c[i] = a[i]
    if lenb:
        for i in range(lenb):c[i] = b[i]
    return c

a = create_random_arrays(8, 100,True, True)
print(a)
b = create_random_arrays(6, 100, True, True)
print(b)
c1 = sorted(a + b)
c = merge_two_sorted_arrays(a, b)
print(c)
print(c1)
print(c1 == c)






