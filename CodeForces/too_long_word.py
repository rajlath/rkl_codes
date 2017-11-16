'''
input
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
output
word
l10n
i18n
p43s
'''
for _ in range(int(input())):
    s = input()
    sl= len(s)
    if sl > 10:
        ans = s[0]+str(sl - 2)+s[-1]
    else:
        ans = s
    print(ans)        
