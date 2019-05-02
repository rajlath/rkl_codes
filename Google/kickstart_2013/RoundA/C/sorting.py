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
        lens = int(inputs[indx])
        indx += 1
        nums = [int(x) for x in inputs[indx].split()]
        indx += 1
        odds, evens = [], []
        for i in nums:
            if i % 2:
                odds.append(i)
            else:
                evens.append(i)
        evens = sorted(evens)[::-1]
        odds  = sorted(odds)
        #print(evens, odds)
        id1 , id2 = 0, 0
        ans = [0] * lens
        for i in range(lens):
            if nums[i] % 2 == 0:
                ans[i] = evens[id1]
                id1 += 1
            else:
                ans[i] = odds[id2]
                id2 += 1
        ans = " ".join(map(str, ans))
        ans1 = "Case #{}: {}".format(test, ans)
        print(ans1, file = outs)
        test += 1

else:
    print("Invalid Input file.")


