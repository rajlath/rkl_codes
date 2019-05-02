

from itertools import groupby
import sys

def get_num_words(num):
    numss = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    succ  = ['','',"double", "triple", "quadruple", "quintuple", "sextuple", "septuple", "octuple", "nonuple", "decuple" ]
    nums = groupby(num)
    rets = []
    for k, g in nums:
        lens = len(list(g))
        if lens == 1:
            rets.append(numss[int(k)])
        else:
            if lens > 10:
                for i in range(lens):
                    rets.append(numss[int(k)])
            else:
                rets.append( succ[lens])
                rets.append(numss[int(k)])
    return " ".join(rets+[" "])


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
        number, pattern = [x for x in inputs[indx].split()]
        indx += 1
        parts = [int(x) for x in pattern.split("-")]
        num_parts = []
        last = 0
        ans = ''
        for i in parts:
            num_parts.append(number[last:i+last])
            last = i+last
        ans = ''
        #print(num_parts)
        for i in num_parts:
            ans += get_num_words(i)
        ans = "Case #{}: {}".format(test, ans)
        #print(ans)
        print(ans, file = outs)
        test += 1


