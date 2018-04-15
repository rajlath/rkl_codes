def minimumFlips(pancakes):
      groupedHeight = 1 + pancakes.count('-+') + pancakes.count('+-')
      groupedHeight -= not pancakes.endswith("-")
      return groupedHeight

in_file = open('B-large-practice.in', 'r')
out_file= open('B-large-practice.out', 'w')
case_cnt= int(in_file.readline().strip())
for case in range(case_cnt):
    current = in_file.readline().strip()
    out_file.write("Case #{}: {}".format(case+1, minimumFlips(current)))
    out_file.write("\n")