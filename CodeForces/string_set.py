
ans  = 'abcdefghijklmnopqrstuvwxyz'
s = input()
i = 0
t = ''
for c in s:
    if i < 26:
        if c <= ans[i]:
            t += ans[i]
            i += 1
        else:
            t += c
    else:
        t += c


print(("-1", t)[i==26])

#aacceeggiikkmmooqqssuuwwyy