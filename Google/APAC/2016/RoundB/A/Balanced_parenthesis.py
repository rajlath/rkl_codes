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
        l, r = [int(x) for x in inputs[indx].strip().split()]
        indx += 1
        sums = 0
        if r == 0 or l == 0:
            sums = 0
        else:
            if l >= r:
                for i in range(1, r + 1):
                    sums += (r - (i - 1))
            else:
                for i in range(1, l + 1):
                    sums += (l - (i - 1))

        ans = "Case #{}: {}".format(test, sums)
        print(ans, file=outs)
        test += 1
else:
    print("Invalid Input File.")


