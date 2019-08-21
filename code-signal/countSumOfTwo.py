from collections import Counter
def countSumOfTwoRepresentations2(n, l, r):
    '''
    Given integers n, l and r, find the number of ways to represent
    n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.
    Example
    For n = 6, l = 2, and r = 4, the output should be
    countSumOfTwoRepresentations2(n, l, r) = 2.
    '''
    counts = 0
    value = Counter(list(range(l, r+1)))
    for i in  value:
        counts += value[n - i]
        counts += (n - i) == i
    return counts // 2

print(countSumOfTwoRepresentations2(6, 3, 3))
