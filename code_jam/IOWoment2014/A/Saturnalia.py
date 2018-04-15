'''
Input

5
Merry Saturnalia, Giovanni!
Equus, you're the best!
Caballus, you try really hard!

w
'''
import re
in_file = open('A-small-practice.in', 'r')
ou_file = open('A-small-practice.ou', 'w')

case_cnt= int(in_file.readline().strip())
for case in range(case_cnt):
    s = in_file.readline().strip("\r\n")
    print(len(s))

    lens =len(s) + 2
    lens = max(3, lens)
    ou_file.write("Case #{}:".format(case+1))
    ou_file.write("\n")
    ou_file.write("+" + "-"*lens + "+")
    ou_file.write("\n")
    ou_file.write("| {} |".format(s))
    ou_file.write("\n")
    ou_file.write("+" + "-"*lens + "+")
    ou_file.write("\n")

