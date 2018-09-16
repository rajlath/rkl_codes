#Highest Value Palindrome

noc, k = [int(x) for x in input().split()]
s = input()
p = list(s)

l = 0
r = noc - 1
while l < r:
    if s[l] != s[r]:
        p[l] = p[r] = max(s[l], s[r])
        k -= 1
    r -= 1
    l += 1

if k < 0: print(-1)
else:
    l = 0
    r = noc - 1
    while l <= r:
        if l == r:
            if k > 0:p[l] = "9"
        if p[l] != "9":
            if k > 2 and p[l] == s[l] and p[r] == s[r]:
                k -= 2
                p[l]= p[r]= '9'
            elif k >= 1 and p[l] != s[l] or p[r] != s[r]:

                k -= 1
                p[l] = p[r] = '9'

        l += 1
        r -= 1
    print("".join(p))




