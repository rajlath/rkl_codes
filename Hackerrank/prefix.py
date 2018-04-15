def prefix(p):
    m = len(p)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j >= 0 and p[j] != p[i]:
            if j - 1 >= 0:
                j = pi[j - 1]
            else:
                j = -1
        j += 1
        pi[i] = j
    return pi

print(prefix("rajram"))