import sys

def get_input_output():
    if len(sys.argv) >= 3:
        ins = open(sys.argv[1], "r")
        out = open(sys.argv[2], "w")
        return (ins, out)
    else:
        return (None, None)

def build(k):
    n = 1
    while k > n:
        n *= 2
    if k == n : return 0
    return 1 - build(n - k)

ins, out = get_input_output()
if ins != None:
    nb_test = int(ins.readline().strip())
    test = 1
    for _ in range(nb_test):
        lens = int(ins.readline().strip())
        answer = build(lens)
        ans  = "Case #{}: {}".format(test, answer)
        print(ans, file=out)
        #ins.readline()
        test += 1
else:
    print("Invalid or no input file selected.")





