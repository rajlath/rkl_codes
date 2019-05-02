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
        noc = int(inputs[indx])
        indx += 1
        names = []
        for _ in range(noc):
            names.append(inputs[indx].strip())
            indx += 1
        names = sorted(names)
        maxs = 0
        wins = ""
        for i in names:
            lens  = len(set([z for z in i if z != ' ']))
            if lens > maxs:
                maxs = lens
                wins = i

        ans = "Case #{}: {}".format(test, wins)
        print(ans, file=outs)
        test += 1
else:
    print("Invalid Input File.")


'''
nb_test = int(input())
for _ in range(nb_test):
    maxs = 0
    name = "Z"
    noc = int(input())
    for _ in range(noc):
        curr = input()
        lens = len(set(curr))
        if lens == maxs:
            if curr < name:
                name = curr
        elif lens > maxs:
            maxs = lens
            name = curr
    print(name)
'''
