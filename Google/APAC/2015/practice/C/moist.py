import sys
from math import asin

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line.strip() for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return None

inputs , outs = get_input_output()
indx = 0
test = 1
if inputs is not None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        nb_names = int(inputs[indx])
        #print(nb_names)
        indx += 1
        count = 0
        last  = ''
        for _ in range(nb_names):
            curr = inputs[indx]
            #print(curr)
            if curr < last:
                count += 1
            else:last = curr
            indx +=1
        ans =  "Case #{}: {}".format(test, count)
        print(ans,  file = outs)
        test += 1

else:
    print("invalid Input file.")

