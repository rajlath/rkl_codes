import time
s = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]

def selection_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_j = i
        for j in range(max_j):
            if seq[j] > seq[max_j]:
                max_j = j
                seq[i], seq[max_j] = seq[max_j], seq[i]

    return seq


n = time.clock()
print(selection_sort(s))
print(time.clock() - n)
