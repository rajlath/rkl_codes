nb_test = int(input())
for _ in range(nb_test):
    nos = int(input())
    string = ''
    for _ in range(nos):
        a, b = [x for x in input().split()]
        string += a * int(b)

    lens = len(string)
    matches = [0] * lens
    dups    = [0] * lens

    for len in range(1, lens):
        stop = lens - len + 1
        for i in range(stop):
            if dups[i]:continue
            for j in range(i+1, stop):
                if string[i:i+len] == string[j:j+len]:
                    continue
                matches[i] += 1
                dups[j] = 1
        if matches[i]:
            print(matches[i] + 1, len, string[:i])


