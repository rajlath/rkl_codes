import sys

def get_input_output():
    if len(sys.argv) >= 3:
        ins = open(sys.argv[1], "r")
        out = open(sys.argv[2], "w")
        return (ins, out)
    else:
        return (None, None)

ins, out = get_input_output()
if ins != None:
    nb_test = int(ins.readline().strip())
    test = 1
    for _ in range(nb_test):
        nb_bus = int(ins.readline().strip())
        touch  = [0 for x in range(5001)]
        lr  = [int(x) for x in ins.readline().strip().split()]
        lr_pair= [(lr[x], lr[x+1]) for x in range(0, nb_bus*2, 2)]
        for i in lr_pair:
            l, r = i[0], i[1]
            for j in range(l, r+1): touch[j] += 1
        nb_query = int(ins.readline().strip())
        curr = []
        for _ in range(nb_query):
            curr.append(touch[int(ins.readline().strip())])
        curr = " ".join(map(str, curr))
        ans  = "Case #{}: {}".format(test, curr)
        print(ans, file=out)
        ins.readline()
        test += 1
else:
    print("Invalid or no input file selected.")





