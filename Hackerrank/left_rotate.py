def rotate(l, n):
    return l[n:] + l[:n]

nos,nor = [(x) for x in input().split()]
ans = rotate([(x) for x in input().split()], int(nor))
print(" ".join(ans))