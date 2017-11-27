'''
https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/game-of-strings-2/

TLE  on all but last test

SAMPLE INPUT
3
setupsetpreset 7
setupsetpreset 8
setupsetpreset 9
SAMPLE OUTPUT
Puchi is a cheat!
set
set
'''
def KMP_fail(s):
    lens = len(s)
    F    = [0] * lens
    F[0] = 0
    j = 0
    for i in range(1, lens):
        while j>0 and s[i] != s[j]:
            j = F[j-1]
        if s[i] == s[j]:
            j += 1
        F[i] = j
    return F

for i in range(int(input())):
    s, k = input().split()
    k = int(k)
    is_cheat = True
    F = KMP_fail(s)
    lens = len(s)
    if F[lens-1] == 0:
        is_cheat = True
    else:
        bb=min(k,lens)
        alwd=F[lens-1]
        v = []
        for j in range(bb):v.append(F[j])
        v = sorted(v)
        while alwd:
            start = 0
            end   = bb - 1
            while start <= end:
                mid = (start + end) // 2
                if v[mid] == alwd:
                    is_cheat = False
                    break
                elif v[mid]<alwd:
                    start = mid + 1
                else:
                    end = mid -1
            if not is_cheat:break
            alwd = F[alwd - 1]

    if is_cheat:
        print("Puchi is a cheat!")
    else:
        for j in range(alwd):
            print(s[j], end="")









