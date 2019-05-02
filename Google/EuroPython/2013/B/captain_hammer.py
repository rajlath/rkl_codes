import sys
import math

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
    nb_test = int(next(ins).strip())
    test_no = 1
    for _ in range(nb_test):
        V, D = [int(x) for x in next(ins).strip().split()]
        g = 9.8
        d = ((D * g ) / V) / V
        d = min(1.0, d)
        a = math.asin(d) / 2
        a *= (180 / math.pi)
        ans = "Case #{}: {:.6f}".format(test_no, a)
        print(ans, file=outs)
        test_no += 1

else:
    print("Invalid IO")



