'''
Examples
inputCopy
5
a
aba
abacaba
ba
aba
outputCopy
YES
a
ba
aba
aba
abacaba
'''
all_str = []
for i in range(int(input())):
    all_str.append(input())
all_str.sort(key = lambda s: len(s))
ans = "YES"
for i in range(1, len(all_str)):
    if not all_str[i-1] in all_str[i]:
        ans = "NO"
        break
print(ans)
if ans == "YES":print("\n".join(all_str))





