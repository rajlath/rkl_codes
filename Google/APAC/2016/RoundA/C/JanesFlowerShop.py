'''
Input
3
2
200 100 100
3
10000 3000 4000 5000
5
3000 100 100 100 100 100

output
Case #1: 0.000000000000
Case #2: 0.088963394693
Case #3: -0.401790748826
'''
import sys


def calc(r, n, a):
    ans = 1
    sums = 0
    for i in range(n+1):
        sums += ans * a[i]
        ans *= r
    return sums

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return (None, None)

inputs , outs = get_input_output()

if inputs is not None:
    indx = 0
    test = 1
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        n = int(inputs[indx])
        indx += 1
        a = [int(x) for x in inputs[indx].split()]
        indx += 1
        a = a[::-1]
        a[n] = -a[n]
        low = 0
        high = 2
        for i in range(200):
            mid = (low + high) * 0.5
            if calc(mid, n, a) < 0: high = mid
            else:low = mid
        ans = "Case #{}: {:.12f}" .format(test, ((low + high) * 0.5 - 1))
        print(ans, file=outs)
        test += 1



