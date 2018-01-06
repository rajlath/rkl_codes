from collections import defaultdict
from itertools import combinations
from random import randint
def triple_with_sum2(a, target=0):
    """Return a tuple of three numbers in the sequence a that sum to
    target (default: 0). Raise NotFoundError if no triple sums to
    target.

    """ 
    positions = defaultdict(set)
    for i, n in enumerate(a):        
        positions[n].add(i)
    for (i, ai), (j, aj) in combinations(enumerate(a), 2):
        n = target - ai - aj        
        if positions[n].difference((i, j)):
            return n, ai, aj
    raise NotFoundError('No triple sums to {}.'.format(target))
cases = 100    
testcases = [randint(-200, 200) for _ in range(100000)]

print(triple_with_sum2(testcases,20))    
    
    
