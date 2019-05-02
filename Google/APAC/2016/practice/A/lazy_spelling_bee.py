import sys

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return (None, None)

MOD = 1000000007
inputs , outs = get_input_output()

if inputs is not None:
    indx = 0
    test = 1
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        ins = inputs[indx].strip()
        indx += 1

        lens = len(ins)
        ans  = 1
        for i in range(lens):
            curs = set()
            if i > 0 : curs.add(ins[i - 1])
            curs.add(ins[i])
            if i < lens - 1: curs.add(ins[i + 1])
            ans = (ans * len(curs)) % MOD
        anss = "Case #{}: {}".format(test, ans)
        print(anss, file = outs)
        test += 1


else:
    print("Invalid or no input file.")





'''
MOD = 1000000007
nb_test = int(input())
for _ in range(nb_test):
    curr = input()
    lens = len(curr)
    ans = 1
    for j in range(lens):
        curs = set()
        if j > 0: curs.add(curr[j - 1])
        curs.add(curr[j])
        if j < lens - 1: curs.add(curr[j + 1])
        ans = (ans * len(curs)) % MOD
    print(ans)
'''
