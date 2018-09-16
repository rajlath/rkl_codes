from collections import Counter
def is_valid(s1,s2):
    #print(s1, s2)
    if s1 == s2:return True
    elif s1 == "a" and s2 == "b": return True
    elif s2 == "a" and s1 == "b": return True
    elif s1 == "z" and s2 == "y": return True
    elif s2 == "z" and s1 == "y": return True
    else:
        #print(s1,s2)
        ord1 = ord(s1)
        ord2 = ord(s2)
        alls = []
        for i in [-1, 1]:
            alls.append(ord1 + i)
            alls.append(ord2 + i)
        alls = Counter(alls)
        #print(alls)
        if 2 in alls.values(): return True
    return False

for _ in range(int(input())):
    lens = int(input())
    words = input()
    l, r = lens//2 - 1, lens // 2
    ans = "YES"
    while l >= 0 and r < lens:
        if not is_valid(words[l], words[r]):
            ans = "NO"
            break
        l-= 1
        r+=1
    print(ans)








