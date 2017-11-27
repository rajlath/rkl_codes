from collections import defaultdict
from itertools import combinations
from random import randint

def selection_sort(seq):
    """Sort the mutable sequence seq in place and return it."""
    for i in reversed(range(len(seq))):
        # Find the index of greatest item in seq[:i+1].
        greatest = 0
        for j in range(1, i + 1):
            if seq[j] > seq[greatest]:
                greatest = j
        seq[i], seq[greatest] = seq[greatest], seq[i]
    return seq
    
def selection_sort_1(seq):
    """Sort the mutable sequence seq in place and return it."""
    for i in reversed(range(len(seq))):
        print(i)
        greatest = max(range(i + 1), key=seq.__getitem__)
        seq[i], seq[greatest] = seq[greatest], seq[i]
    return seq
    
testcases = [randint(30, 200) for _ in range(100)] 
print(min(testcases),max(testcases))
seq = selection_sort_1(testcases)
print(seq[0],seq[-1])   
    
        
