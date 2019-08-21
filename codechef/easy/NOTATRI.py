lens = int(input())
while lens != 0:
    elems = sorted([int(x) for x in input().split()], reverse = True)
    counts = 0
    for i in range(lens):
        a = i
        b = i + 1
        c = lens - 1
        while b < c:
            if elems[b] + elems[c]  < elems[a]:
                counts += (c - b)
                c -= 1
            else:
                b += 1
    print(counts)    
    lens = int(input())