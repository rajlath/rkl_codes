#Numbers Wanted
#https://www.codechef.com/NACA2019/problems/NUMTED

from collections import defaultdict
def get_largest_unique_char_lens(s):
    last = -1
    answ =  1
    cnts =  defaultdict(int)
    i = 0
    for c in s:
        if c in cnts:last = max(last, cnts[c])
        answ = max(answ, i - last)
        cnts[c] = i
        i += 1
    #print(cnts)
    return answ

#print(get_largest_unique_char_lens("ABCADEFGH"))
nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    strA = input()
    strB = input()
    lenA = get_largest_unique_char_lens(strA)
    lenB = get_largest_unique_char_lens(strB)
    if lenA > lenB:print("AG")
    else:print("AB")





