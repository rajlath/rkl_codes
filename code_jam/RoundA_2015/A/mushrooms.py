in_file = open("A-large-practice.in", "r")
ou_file = open("A-large-parctice.ou", "w")

nos_test_case = int(in_file.readline().strip())
for case in range(nos_test_case):
    noe_elem  = int(in_file.readline().strip())
    on_plate  = [int(x) for x in in_file.readline().strip().split()]
    min_eat   = 0
    for i in range(noe_elem-1):
        min_eat += (max(0, on_plate[i]-on_plate[i+1]))
    ans_a = min_eat

    max_rate = 0
    for i in range(1, noe_elem):
        max_rate = max(max_rate, on_plate[i-1] - on_plate[i])
    min_eat = 0
    for i in range(noe_elem-1):
        min_eat += min(on_plate[i], max_rate)
    ans_b = min_eat

    ou_file.write("Case #{}: {} {}".format(case+1, ans_a, ans_b))
    ou_file.write("\n")




