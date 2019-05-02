'''
Problem

You are hosting a party with G guests and notice that there is an odd number of guests!
When planning the party you deliberately invited only couples and gave each couple a unique number C on their invitation.
You would like to single out whoever came alone by asking all of the guests for their invitation numbers.

Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will be:

One line containing the value G the number of guests.
One line containing a space-separated list of G integers. Each integer C indicates the invitation code of a guest.
Output

For each test case, output one line containing "Case #x: " followed by the number C of the guest who is alone.

Limits

1 ≤ N ≤ 50
0 < C ≤ 2147483647
Small dataset

3 ≤ G < 100
Large dataset

3 ≤ G < 1000
Sample


Input

3
3
1 2147483647 2147483647
5
3 4 7 4 3
5
2 10 2 10 5

Output
Case #1: 1
Case #2: 7
Case #3: 5
'''


import sys
from collections import Counter

def get_input_out():
    args = sys.argv
    if len(args) >= 2:
        ins = open(sys.argv[1], "r")
        in_puts = [line for line in ins.readlines()]
        outs = open(sys.argv[2], "w")
        return (in_puts, outs)
    return (None, None)

ins, outs = get_input_out()
if ins is not None:
    index = 0
    tests = 1

    nb_test = int(ins[index])
    index += 1
    for _ in range(nb_test):
        nb_number = int(ins[index].strip())
        index += 1
        numbers = Counter([x for x in ins[index].strip().split()])
        index += 1
        for i in numbers:
            if numbers[i] == 1:
                ans = i
                break
        ans = "Case #{}: {}".format(tests, ans)
        print(ans, file = outs)
        tests += 1







