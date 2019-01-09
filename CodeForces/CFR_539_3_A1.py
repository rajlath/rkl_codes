n = int(input())
s = input()
indx = 0
gap  = 1
decoded = ''
while indx < n:
    decoded += s[indx]
    indx += gap
    gap += 1
print(decoded)
