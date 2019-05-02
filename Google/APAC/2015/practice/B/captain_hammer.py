import sys
from math import asin

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return None

inputs , outs = get_input_output()
indx = 0
test = 1
pi = 3.141592653
g = 9.8
if inputs is not None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        V, D = map(float, inputs[indx].split())
        indx += 1
        tmp = D * 9.8 / (V * V)
        if tmp > 1.0:tmp = 1.0
        al = asin (tmp) / pi * 180.0
        ans = al / 2
        print("Case #{}: {:.7}".format(test,ans), file = outs)
        test += 1

else:
    print("invalid Input file.")

