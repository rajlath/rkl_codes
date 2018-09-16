import time
from collections import defaultdict


def insertion_sort(seq):
    if len(seq) < 2: return seq
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j] < seq[j-1]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq

def selection_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(max_j):
            if seq[j] > seq[max_j]:
                max_j = j
                seq[i], seq[max_j] = seq[max_j], seq[i]

    return seq

def gnome_sort(seq)    :
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i -= 1

    return seq


def count_sort_dict(a):
    b, c = [], defaultdict(list)
    for x in a:
        c[x].append(x)
    for k in range(min(c), max(c) + 1):
        b.extend(c[k])
    return b



'''
def merge_sort_n(left,right):
    if not left or not right:return left or right
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1
    if i < len(left) - 1 : result+=left[i:]
    elif j < len(right) - 1 : result += right[j:]
    return result
    '''



def quick_sort(seq):
    if len(seq) < 2: return seq
    mid = len(seq)//2
    piv = seq[mid]
    seq = seq[:mid] + seq[mid+1:]
    lo = [ x for x in seq if x <= piv]
    hi = [ x for x in seq if x >  piv]
    return quick_sort(lo) + [piv] + quick_sort(hi)

import heapq
def heap_sort_hq(seq):
    a = []
    for i in seq:
        heapq.heappush(a, i)
    return [heapq.heappop(a) for i in range(len(a))]






s = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]


n1 = time.clock()
s1 = s[:]
print(insertion_sort(s1))
print(time.clock() - n1)

n2 = time.clock()
s2 = s[:]
print(selection_sort(s2))
print(time.clock() - n2)

n3 = time.clock()
s3 = s[:]
print(gnome_sort(s3))
print(time.clock() - n3)

n4 = time.clock()
s4 = s[:]
print(count_sort_dict(s4))
print(time.clock() - n4)

n5 = time.clock()
s5 = s[:]
print(quick_sort(s5))
print(time.clock()  - n5)

n6 = time.clock()
s6 = s[:]
print(quick_sort(s6))
print(time.clock()  - n6)




