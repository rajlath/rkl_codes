s = input()
cs= set()
for i in range(len(s)):
    s = s[-1] + s[:-1]
    cs.add(s)
print(len(cs))
