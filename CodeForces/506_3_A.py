n, k = [int(x) for x in input().split()]
s    = input()
indx = 1
while indx < n and s[indx:]!= s[:-indx]:indx += 1
print(s[:indx] * (k) + s[indx:])