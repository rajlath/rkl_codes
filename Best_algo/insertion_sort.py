import time
s = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]

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

n = time.clock()
print(insertion_sort(s))
print(time.clock() - n)
n = time.clock()
print(selection_sort(s))
print(time.clock() - n)
