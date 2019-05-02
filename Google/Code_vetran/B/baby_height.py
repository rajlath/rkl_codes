import re
def in_inches(st):
    st = st.replace("'",' ').replace('"', " ")
    numbers = re.findall('\d+', st)
    mf, mi, df, di = numbers
    mom = int(mf) * 12 + int(mi)
    dad = int(df) * 12 + int(di)
    return (mom, dad)

import sys
from collections import defaultdict

def get_input_output_object():
    args = sys.argv
    if len(args) > 2:
        file_ins = open(sys.argv[1], "r")
        in_iter  = iter(file_ins.readlines())
        file_out = open(sys.argv[2], "w")
        return (in_iter, file_out)
    else:
        return (None, None)

ins, outs = get_input_output_object()
if ins != None:
    nb_test = int(next(ins))
    for t in range(nb_test):
        inpu = next(ins)
        sex  = inpu[0]
        mom, dad = in_inches(inpu)
        if sex == "G": mom -= 5
        else:
            dad += 5
        mid = (mom + dad ) / 2
        ranges = [3.5, 4][mid == int(mid)]
        low, high = mid - ranges, mid + ranges
        lowf, lowi = int(low//12), int(low%12)
        lows = str(lowf) +"'"+str(lowi)+'"'
        highf, highi = int(high//12), int(high%12)
        highs = str(highf)+"'"+str(highi)+'"'
        ans = "Case #{}: {} to {}".format(t + 1, lows, highs)
        print(ans, file = outs)






