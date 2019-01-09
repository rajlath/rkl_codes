i = 0
lens = int(input())
ins  = input()
decoded = ''
nexts = 0
while nexts < lens:
    nexts = (i * (i + 1)) // 2
    #print(nexts)
    if nexts < lens:
        decoded += ins[nexts]
    else:
        break
    i += 1
print(decoded)



