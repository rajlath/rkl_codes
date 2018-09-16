'''
s = input()
if s[-1] not in "aeioun":print("NO")
else:
    ans = "YES"
    for i in range(len(s)-1):
        if s[i] not in "aeiou":
            if s[i] is not "n" and i < len(s)-1:
                if s[i+1] not in "aeiou":
                    ans = "NO"
                    break

    print(ans)
'''
v='aouie'
s=input()+'b'
#print(list(zip(s, s[1:])))
print(('NO','YES')[all(x in v+'n' or y in v for x,y in zip(s,s[1:]))])






