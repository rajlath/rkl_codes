'''
Input
5
0
1
2
11
1692
Output
Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076
'''

in_file = open('A-large-practice.in', 'r')
out_file= open('A-large-practice.out', 'w')
case_cnt= int(in_file.readline().strip())
for case in range(case_cnt):
    current = int(in_file.readline().strip())
    ans = "INSOMNIA"
    if current:
        num_set = set()
        mult = 1
        while len(num_set) != 10:
            ans  = current * mult
            mult += 1
            for x in str(ans):
                num_set.add(x)
            if len(num_set)==10:
                break

    out_file.write("Case #{}: {}".format(case+1, ans))
    out_file.write("\n")










