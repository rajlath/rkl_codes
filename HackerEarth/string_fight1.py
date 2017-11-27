'''
https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/string-fight-2/description/#
SAMPLE INPUT
2
1 2
212
4 5
55555
SAMPLE OUTPUT
4
2
'''
from sys import stdin, stdout

def get_int_arr():
    return list(map(int, stdin.readline().split()))

def get_counts(s, ss, match_count):
    if match_count == 0:return 0

    match_indx = []
    counts = 0
    for i, v in enumerate(s):
        if v == ss:
            counts += 1
            match_indx.append(i)
    valid_count = 0
    for i in range(match_count - 1, len(match_indx)):
        start_idx = i - (match_count-1)
        if start_idx >= 1:
            left_count = match_indx[start_idx] - match_indx[start_idx-1] - 1
        else:
            left_count = match_indx[start_idx]
        if i+1 < len(match_indx):
            right_count = match_indx[i+1] - match_indx[i] - 1
        else:
            right_count = len(s) - match_indx[i] - 1

        valid_count += (left_count + 1) * (right_count + 1)
    return valid_count

for  _ in range(int(input())):
    match_count, chs = get_int_arr()
    chs = str(chs)
    s = input()
    ans = get_counts(s, chs, match_count)
    print(ans)








