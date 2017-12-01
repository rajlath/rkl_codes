'''
Problem

A and B are the only two candidates competing in a certain election. We know from polls that exactly N voters support A, and exactly M voters support B. We also know that N is greater than M, so A will win.

Voters will show up at the polling place one at a time, in an order chosen uniformly at random from all possible (N + M)! orders. After each voter casts their vote, the polling place worker will update the results and note which candidate (if any) is winning so far. (If the votes are tied, neither candidate is considered to be winning.)

What is the probability that A stays in the lead the entire time -- that is, that A will always be winning after every vote?

Input

The input starts with one line containing one integer T, which is the number of test cases.
Each test case consists of one line with two integers N and M: the numbers of voters supporting A and B,
respectively.

Output

For each test case, output one line containing Case #x: y,
where x is the test case number (starting from 1) and y is the probability that
A will always be winning after every vote.
y will be considered correct if y is within an absolute or relative error of 10-6 of the correct answer.

Limits

1 ≤ T ≤ 100.
Small dataset

0 ≤ M < N ≤ 10.
Large dataset

0 ≤ M < N ≤ 2000.

Sample
Input
2
2 1
1 0

Output
Case #1: 0.33333333
Case #2: 1.00000000

'''
in_file = open("B-small-practice.in", "r")
ou_file = open("B-small-practice.out","w")
no_cases = int(in_file.readline())
for i in range(no_cases):
    m, n = [int(x) for x in in_file.readline().strip().split()]
    ans = (m - n) / (m + n)
    ou_file.write("Case #%d: %.8f" % (i+1, ans))
    ou_file.write("\n")

