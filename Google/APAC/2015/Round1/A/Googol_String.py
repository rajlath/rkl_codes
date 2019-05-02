import sys

N = 62
ar = [0 for x in range(N)]
ar[0] = 1
for i in range(1, N):
    ar[i] = 2 * ar[i - 1]


def get_ans(a, i, rev)    :
    global ar
    if a == 1: return rev
    if a < ar[i]:return get_ans(a, i - 1, rev)
    elif a > ar[i]:return get_ans(ar[i + 1] - a, i - 1, 1 - rev)
    else:return rev




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
if inputs is not None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        curr = int(inputs[indx])
        indx += 1
        ans = get_ans(curr, 60, 0)
        ans = "Case #{}: {}".format(test, ans)
        print(ans, file = outs)
        test += 1







