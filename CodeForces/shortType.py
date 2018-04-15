'''
7
abcabca
output
5
inputCopy
8
abcdefgh
output
8
'''
def shorten(s):
    for i in range(len(s)):
        if s[:i] == s[i:i+i]:
            s = s[i+i:]
    return s

noe = int(input())
s = input()
keyed = 0
while True:
    l = len(s)
    s = shorten(s)
    if l == len(s):
        break
    keyed += (l - len(s))//2 + 1
keyed += len(s)
print(keyed)


