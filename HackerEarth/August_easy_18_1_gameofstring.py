from string import ascii_uppercase as uc
table = uc + uc
n = int(input())
s = input()
t = input()
days = 0
for i in range(n):
    ac = s[i]
    bc = t[i]
    ai = table.find(ac)
    bi = table.find(bc, ai)
    diff = bi - ai
    d, r = divmod(diff, 13)
    days += (d + r)
    #print(days)
print(days)

