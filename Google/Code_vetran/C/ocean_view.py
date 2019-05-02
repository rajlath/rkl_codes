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
        lens = int(next(ins))
        heights = [int(x) for x in next(ins).split()]
        max_now = heights[0]
        destroy = 0
        for i in range(1, lens):
            if heights[i] < max_now:
                destroy += 1
            else:
                max_now = max(max_now, heights[1])
        ans = "Case #{}: {}".format(t+1, destroy)
        print(ans, file=outs)