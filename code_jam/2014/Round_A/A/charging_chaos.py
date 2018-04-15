'''
Problem
Shota the farmer has a problem. He has just moved into his newly built farmhouse, but it turns out that the outlets haven't been configured
correctly for all of his devices. Being a modern farmer, Shota owns a large number of smartphones and laptops, and even owns a tablet for
his favorite cow Wagyu to use. In total, he owns N different devices.

As these devices have different specifications and are made by a variety of companies, they each require a different electric flow to charge.
Similarly, each outlet in the house outputs a specific electric flow. An electric flow can be represented by a string of 0s and 1s of length L.

Shota would like to be able to charge all N of his devices at the same time. Coincidentally, there are exactly N outlets in his new house.
In order to configure the electric flow from the outlets, there is a master control panel with L switches. The ith switch flips the ith bit of
the electric flow from each outlet in the house. For example, if the electric flow from the outlets is:

Outlet 0: 10
Outlet 1: 01
Outlet 2: 11
Then flipping the second switch will reconfigure the electric flow to:

Outlet 0: 11
Outlet 1: 00
Outlet 2: 10
If Shota has a smartphone that needs flow "11" to charge, a tablet that needs flow "10" to charge, and a laptop that needs flow "00" to charge,
then flipping the second switch will make him very happy!

Misaki has been hired by Shota to help him solve this problem. She has measured the electric flows from the outlets in the house,
and noticed that they are all different. Decide if it is possible for Shota to charge all of his devices at the same time, and if
it is possible, figure out the minimum number of switches that needs to be flipped, because the switches are big and heavy and Misaki
doesn't want to flip more than what she needs to.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of three lines.
The first line contains two space-separated integers N and L. The second line contains N space-separated strings of length L,
representing the initial electric flow from the outlets. The third line also contains N space-separated strings of length L,
representing the electric flow required by Shota's devices.

Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the minimum number of
switches to be flipped in order for Shota to charge all his devices. If it is impossible, y should be the string "NOT POSSIBLE"
(without the quotes). Please note that our judge is not case-sensitive, but it is strict in other ways: so although "not  possible" will be
judged correct, any misspelling will be judged wrong. We suggest copying/pasting the string NOT POSSIBLE into your code.

Limits
1 ≤ T ≤ 100.
No two outlets will be producing the same electric flow, initially.
No two devices will require the same electric flow.
Small dataset
1 ≤ N ≤ 10.
2 ≤ L ≤ 10.

Large dataset
1 ≤ N ≤ 150.
10 ≤ L ≤ 40.

Sample

Input

3
3 2
01 11 10
11 00 10
2 3
101 111
010 001
2 2
01 10
10 01

Output
Case #1: 1
Case #2: NOT POSSIBLE
Case #3: 0

'''
#helpers
def get_diff(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]

def flip(ori, diff):
    ori = list(ori)
    for i in diff:
        ori[i] = "0" if ori[i]=="1" else "1"
    return "".join(ori)

def is_equal(a, b):
    for x, y in zip(a, b):
        if x != y:
            return False
    return True

#solve

in_file = open("A-small-practice.in")
out_file= open("A-small-practice.out","w")
no_test_case = int(in_file.readline().strip())

for i in range(no_test_case):
    ans = "Case #{}: ".format(i+1)
    noe, loe = [int(x) for x in in_file.readline().strip().split()]
    has = [x for x in in_file.readline().strip().split()]
    need= [x for x in in_file.readline().strip().split()]
    need = sorted(need)

    best = loe + 1
    for j in range(noe):
        diff = get_diff(has[j], need[0])
        #print(has[j], need[0], diff)
        if len(diff) >= best:continue
        flipped_has = [flip(o, diff) for o in has]
        #print(flipped_has)
        flipped_has = sorted(flipped_has)
        if is_equal(flipped_has, need):
            best = len(diff)
    if best == loe + 1:
        ans += "NOT POSSIBLE"
    else:
        ans += str(best)
    out_file.write(ans)
    out_file.write("\n")


