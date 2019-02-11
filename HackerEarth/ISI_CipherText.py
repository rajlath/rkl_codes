from collections import Counter
lens = int(input())
encoded = input()
encc    = Counter(encoded)
offset  = ord(encc.most_common()[0][0]) - ord('n')
ans = ''
for i in encoded:
    ans += chr((ord(i) - ord('a') - offset + 26) % 26 + ord('a'))
print(ans)
