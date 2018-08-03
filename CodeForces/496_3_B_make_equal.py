a = input()[::-1]
b = input()[::-1]
same = 0
for i in range(min(len(a), len(b))):
    if a[i] != b[i]:
        break
    else:same +=1
print(len(a) - same + len(b) - same)





