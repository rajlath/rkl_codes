
def alphabetSubsequence(s):
    a="abcdefghijklmnopqrstuvwxyz"
    i=0
    j=0
    while i<len(s) and j<len(a):
        if a[j] == s[i]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s)

print(alphabetSubsequence("eft"))