from collections import Counter
wc = lambda x: sum([1 for  y in x if y.isalpha()])
for _ in range(int(input())):
    inps = input()
    q = int(input())
    for _ in range(q):
        qr = [x for x in input().split()]
        if len(qr) == 2 and qr[0] == "1":
            word = qr[1]
            inps += " " + word
        else:
            if qr[0] =="2":
               inc = Counter(inps.split())
               maxs = sorted([x for x in inc if inc[x] == max(inc.values())])
               print(maxs[0])
            else:
                print(wc(inps))
