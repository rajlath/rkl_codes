'''
Problem
A "0/1 string" is a string in which every character is either 0 or 1.
There are two operations that can be performed on a 0/1 string:
switch: Every 0 becomes 1 and every 1 becomes 0. For example, "100" becomes "011".
reverse: The string is reversed. For example, "100" becomes "001".
Consider this infinite sequence of 0/1 strings:

S0 = ""
S1 = "0"
S2 = "001"
S3 = "0010011"
S4 = "001001100011011"
...
SN = SN-1 + "0" + switch(reverse(SN-1)).
You need to figure out the Kth character of Sgoogol, where googol = 10100.

Input
The first line of the input gives the number of test cases, T. Each of the next T lines contains a number K.
Output
For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the Kth character of Sgoogol.

Limits
1 ≤ T ≤ 100.
Small dataset
1 ≤ K ≤ 105.
Large dataset
1 ≤ K ≤ 1018.

Sample
Input
4
1
2
3
10

Output
Case #1: 0
Case #2: 0
Case #3: 1
Case #4: 0
'''

import os
fins = os.path.join(os.path.dirname(__file__), "B-small-practice.in")
fout = os.path.join(os.path.dirname(__file__), "B-small-practice.out")


in_file = open(fins, "r")
out_file= open(fout, "w")



def solve(n, k):
    if k < (1 << (n-1)):
        return solve(n-1, k)
    elif k == (1 << (n-1)):
        return 0
    return 1 - solve(n-1, ((1 << n) - k))


nb_test = int(in_file.readline().strip())

for case in range(nb_test):
    n =  int(in_file.readline().strip())
    ans = solve(60, n)
    out_file.write("Case #{}: {}".format(case+1, ans))
    out_file.write("\n")
