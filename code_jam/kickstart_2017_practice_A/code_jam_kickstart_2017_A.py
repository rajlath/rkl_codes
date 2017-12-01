'''
Problem

The Constitution of a certain country states that the leader is the person with the name containing the greatest number of different alphabet letters. (The country uses the uppercase English alphabet from A through Z.) For example, the name GOOGLE has four different alphabet letters: E, G, L, and O. The name APAC CODE JAM has eight different letters. If the country only consists of these 2 persons, APAC CODE JAM would be the leader.

If there is a tie, the person whose name comes earliest in alphabetical order is the leader.

Given a list of names of the citizens of the country, can you determine who the leader is?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line with an interger N, the number of people in the country. Then N lines follow. The i-th line represents the name of the i-th person. Each name contains at most 20 characters and contains at least one alphabet letter.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the name of the leader.
Limits

1 ≤ T ≤ 100.
1 ≤ N ≤ 100.
Small dataset

Each name consists of at most 20 characters and only consists of the uppercase English letters A through Z.

Large dataset

Each name consists of at most 20 characters and only consists of the uppercase English letters A through Z and ' '(space).
All names start and end with alphabet letters.
Sample


Input

Output

2
3
ADAM
BOB
JOHNSON
2
A AB C
DEF

Case #1: JOHNSON
Case #2: A AB C


'''

in_file = open("A-large-practice.in")
out_file= open("Ans_kickstart_2017_A_large.out","w")
no_test_case = int(in_file.readline().strip())

for i in range(no_test_case):
    vec = []
    curr_winner = (0,'')
    for _ in range(int(in_file.readline().strip())):
        s = in_file.readline()
        l = len(set(s.replace(" ",'')))
        vec.append((l, s))
    anss = sorted(vec, key=lambda tup: (tup[0],tup[1]) )
    temp=anss[-1][0]
    for j in range(len(anss)):
        if anss[j][0] == temp:
            ans = anss[j][1]
            break
    out_file.write("Case #{}: {}".format(i+1, ans))

