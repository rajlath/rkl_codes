seq1 = [1,2,3,5,7,8]
seq2 = [3,5,6]

def intersection_two_arrays_1(seq1, seq2):
    return set(seq1).intersection(set(seq2))

def intersection_two_arrays_2(seq1, seq2):
    return list(set(seq1) & set(seq2))

def intersection_two_arrays_3(seq1, seq2):

    #using merge soft

    rets = []
    while seq1 and seq2:
        if seq1[-1] == seq2[-1]:
            rets = [(seq1.pop())]+rets
            seq2.pop()
        elif seq1[-1] > seq2[-1]:
            seq1.pop()
        else:
            seq2.pop()
    return rets










print(intersection_two_arrays_1(seq1, seq2))
print(intersection_two_arrays_2(seq1, seq2))
print(intersection_two_arrays_3(seq1, seq2))
