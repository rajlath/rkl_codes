import sys

def get_input_output():
    if len(sys.argv) >= 3:
        ins = open(sys.argv[1], "r")
        out = open(sys.argv[2], "w")
        return (ins, out)
    else:
        return (None, None)



ins, out = get_input_output()
RW  = lambda : ins.readline().strip()
if ins != None:
    nb_test = int(RW())
    test = 1
    for _ in range(nb_test):
        lens = int(RW())
        src_tgt = [(RW(), RW())  for _ in range(lens)]
        tour = {}
        begs = set()
        ends = set()
        for i in src_tgt:
            tour[i[0]] = i[1]
            begs.add(i[0])
            ends.add(i[1])
        answer = [list(begs - ends)[0]]
        for _ in range(lens):
            answer.append(tour[answer[-1]])
        answer = ' '.join("{}-{}".format(answer[i], answer[i+1]) for i in range(lens))
        ans  = "Case #{}: {}".format(test, answer)
        print(ans, file=out)
        test += 1
else:
    print("Invalid or no input file selected.")





