'''
2
ab
abab
ab
aabb
'''
import re
for _ in range(int(input())):
    p = input()
    t = input()
    cnt = 0
    cnt = 0
    s = t
    while True:
        lens = len(s)
        s = re.sub(p, '', s)
        if len(s) == lens:
            break

    print((len(t) - len(s)) // len(p))