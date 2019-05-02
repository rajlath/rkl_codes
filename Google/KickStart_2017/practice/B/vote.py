import sys

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return (None, None)


inputs , outs = get_input_output()
indx = 0
test = 1

if inputs != None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        n, m = [int(x) for x in inputs[indx].strip().split()]
        indx += 1
        numerators = float(n) - float(m)
        denominaor = float(n) + float(m)
        ans = numerators / denominaor
        ans = "Case #{}: {:15.12f}".format(test, ans)
        print(ans, file=outs)
        test += 1
else:
    print("Invalid Input File.")


