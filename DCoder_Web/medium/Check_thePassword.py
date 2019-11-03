lens = int(input())
passwords = [input() for x in range(lens)]
sortedpw  = [sorted(x) for x in passwords]
for i,v in enumerate(sortedpw):
    if sortedpw.count(v) >=2:
        l = len(passwords[i])
        print(l, passwords[i][l//2])
        break



