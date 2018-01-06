set3 = "wertyuiop"
set2 = "asdfghjkl"
set1 = "zxcvbnm"

'''
1. For the first letter return the 3rd letter counting right from it's position from the same
   set( i.e. if first letter is in Set 1 return letter from the same.)
2. For the second letter return the 2nd letter counting left from it's position from the next
   set( i.e. if second letter is in Set 1 return letter from the Set 2.)
3. For the third letter return the 1st letter counting left from it's position from the previous
   set( i.e. if third letter is in Set 1 return letter from the Set 3)
4. for the fourth letter return the letter in the same position from the next
   set( i.e. if fourth letter is in Set 1 return letter from the Set 2)
'''

def remove_duplicates(s):
    seen = []
    outs = ""
    for i in s:
        if i in seen:
            continue
        else:
            outs += i
            seen.append(i)
    return outs

def getch(ch, indx):

    for i, v in enumerate(sets):
        if ch in v:
            ci = v.index(ch)
            si = sets.index(v)
            if indx == 0:
                pos = (ci + 3) % len(v)
                return v[pos]
            if indx == 1:
                v = sets[(si+1)%3]
                pos = (ci -2 + len(v)) % len(v)
                return v[pos]
            if indx == 2:
                v = sets[(si -1 + 3)%3]
                pos = (ci -1 + len(v)) % len(v)
                return v[pos]
            if indx == 3 :
                v = sets[(si + 1)%3]
                pos = ci
                return v[pos%len(v)]






sets = ["qwertyuiop","asdfghjkl","zxcvbnm"]

for _ in range(int(input())):
    si = input().strip()
    s = remove_duplicates(si)
    dots = len(si) - len(s)
    out = ""
    for i,v  in enumerate(s):
        outs = getch(v, i%4 )
        out += outs
    print(out +"."*dots)






