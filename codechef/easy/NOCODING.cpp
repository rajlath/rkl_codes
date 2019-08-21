from string import ascii_lowercase as lc
for _ in range(int(input())):
    word = [x for x in input]
    count = 1
    last = word[0]
    for i in word[1:]:
        diff = lc.index(i) - lc.index(last)
        if diff >= 0:
            count += 1 + diff
        else:
            count += 27 + diff
        last = i
    if count <= len(word) * 11:
        print("YES")
    else:
        print("NO")



