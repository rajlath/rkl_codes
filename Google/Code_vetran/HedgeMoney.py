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
        nb_elems = int(next(ins))
        elem = [int(x) for x in next(ins).split()]
        for i in range(1, nb_elems - 1):
            mid = (elem[i - 1] + elem[i + 1]) / 2
            elem[i] =  min(mid, elem[i])
        ans = "Case #{}: {:.6f}".format(t + 1, elem[-2])
        print(ans, file = outs)
else:
    print("Invalid IO")


'''
nb_test = int(input())
for i in range(nb_test):
    lens = int(input())
    elem = [int(x) for x in input().split()]
    for j in range(1, lens-1):
        mid = (elem[j - 1] + elem[j + 1]) / 2
        print(elem[j], mid)
        elem[j] = min(mid, elem[j])
    print("Case #{}: {}".format(i+1, elem[-2]))
'''

