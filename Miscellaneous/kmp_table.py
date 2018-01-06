def kmp_table(pattern):
    """Compute the "next" table corresponding to pattern, for use in the
    Knuth-Morris-Pratt string search algorithm.

    """
    m = len(pattern)
    next = [-1] * m
    j = -1
    for i in range(1, m):
        while j > -1 and pattern[i-1] != pattern[j]:
            j = next[j]
        j += 1
        if pattern[i] != pattern[j]:
            next[i] = j
        else:
            next[i] = next[j]
    return next
    
print(kmp_table("abacab"))    
