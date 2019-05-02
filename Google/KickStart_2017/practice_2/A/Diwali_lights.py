import sys

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
        deco = inputs[indx].strip()
        lens = len(deco)
        indx += 1
        l, r = [int(x) - 1 for x in inputs[indx].strip().split()]
        indx += 1
        bcnts = sum([1 for x in deco if x == "B"])
        ans   = 0
        ans += (r - l) // lens * bcnts
        r = (r - l) % lens + l
        for y in range(l, r + 1):
            if deco[y % lens] == "B":ans += 1

        ans = "Case #{}: {}".format(test, ans)
        print(ans, file=outs)
        test += 1
else:
    print("Invalid Input File.")


