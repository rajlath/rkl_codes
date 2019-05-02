import sys
from collections import defaultdict

def get_input():
    if len(sys.argv) > 1:
        fileObj = open(sys.argv[1], "r")
        lines   = [line for line in fileObj.readlines()]
        return lines
    return None


def process(pairs, outs, test)    :

    m = len(pairs)
    n = 0
    colors = defaultdict(int)
    graph  = defaultdict(list)
    for i in pairs:
        src, tgt = i.split()
        if src not in colors:
            colors[src] = -1
            n += 1
        if tgt not in colors:
            colors[tgt] = -1
            n += 1
        graph[src].append(tgt)
        graph[tgt].append(src)
    #print(list(graph))
    ans = True

    while ans and n > 0:
        queue = []
        node  = ''
        o = 0
        for item in colors:
            if colors[item] < 0:
                node = item
                break
        colors[node] = o
        queue.append(node)
        n -= 1
        while ans and queue:
            node = queue.pop(0)
            o = 1 - colors[node]
            for item in graph[node]:
                if colors[item] < 0:
                    colors[item] = o
                    queue.append(item)
                    n -= 1
                elif colors[item] != o:
                    ans = False
                    break
        res = "Case #{}: {}".format(test, ["No", "Yes"][ans])
        print(res , file = outs)


inputs = get_input()
outs   = open(sys.argv[2], "w")
indx = 0
test = 1
if inputs is not None:
    nb_test = int(inputs[indx])
    indx += 1
    for _ in range(nb_test):
        nb_pairs = int(inputs[indx])
        indx += 1
        pairs = []
        for _ in range(nb_pairs):
            pairs.append(inputs[indx].strip())
            indx += 1
        '''processing for individual test'''
        process(pairs, outs, test)
        test += 1

else:
    print("invalid Input file.")

