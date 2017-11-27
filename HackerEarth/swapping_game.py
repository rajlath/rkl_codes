'''
SAMPLE INPUT
3
hrrkhceaate
SAMPLE OUTPUT
hackerearth
'''

def jumble(s):
    outs = [""]* len(s)
    ends = len(s)-1
    begs = 0
    for i in range(len(s)):
        if i%2:
            outs[ends] = s[i]
            ends -= 1
        else:
            outs[begs] = s[i]
            begs += 1
    return outs

swaps = int(input())
s = input()
os = s
repeating = False
done = 0
for i in range(swaps):
    s = "".join(jumble(s))
    done += 1
    if os == s:
        repeating = True
        break
if repeating:
    s = os
    for i in range(swaps%done):
        s = "".join(jumble(s))
print(s)


