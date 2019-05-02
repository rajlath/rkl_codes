import sys

def get_input_output():
    if len(sys.argv) > 2:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        outobj  = open(sys.argv[2], "w")
        return (lines, outobj)
    return (None, None)

def proc(x, n)    :
    i = 0
    while n > 0:
        n -= x ** i
        i += 1
    return n == 0


inputs , outs = get_input_output()
indx = 0
test = 1

if inputs != None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        curr = int(inputs[indx])
        indx += 1
        ans = curr - 1
        for i in range(2, 64):
            maybe = int(curr ** (1.0/i))
            if maybe > 1:
                if proc(maybe, curr):ans = maybe
            else:break

        ans = "Case #{}: {}".format(test, ans)
        print(ans, file=outs)
        test += 1
else:
    print("Invalid Input File.")


