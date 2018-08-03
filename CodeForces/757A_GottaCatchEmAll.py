'''
Examples
inputCopy
Bulbbasaur
outputCopy
1
inputCopy
F
outputCopy
0
inputCopy
aBddulbasaurrgndgbualdBdsagaurrgndbb
outputCopy
2

required = {"B":1, "u":2, "l" : 1, "b" : 1, "a" : 2, "s" : 1, "r" : 1}
s = input()
has = {}
for i in s:
    has[i] = has.get(i, 0) + 1
B_count = s.count("B")

can = 0
for i in range(1, B_count+1):
    cannot = False
    for k, v in required.items():
        if k in has and  v * i <= has[k]:
               continue
        else:
            cannot = True
            break
    if cannot:break
    can += 1
print(can)
'''
s = input()
c = [s.count(x) for x in "Bulbasur"]
c[1] //= 2
c[4] //= 2
print(min(c))

