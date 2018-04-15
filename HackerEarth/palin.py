s = input()
f=lambda s:len(s)if s==s[::-1]else max(f(s[1:]),f(s[:-1]))
print(f(s))