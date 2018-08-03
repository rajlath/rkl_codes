#!/bin/python3

import os
import sys

# Complete the maximumSuperiorCharacters function below.
def maximumSuperiorCharacters(freq):
    numElements=sum(freq);
    bestCase=int((numElements-1)/2);
    smallNum=0;
    separators=numElements-bestCase;
    for i in range(len(freq)):
        if smallNum+freq[i]>separators:
            break;
        else:
            smallNum+=freq[i];
    problemNum=smallNum+freq[i]-separators;
    if problemNum<smallNum:
        return bestCase;
    elif (smallNum>1):
        return bestCase-(problemNum-smallNum+1);
    else:
        return numElements-smallNum-freq[i];


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        freq = list(map(int, input().rstrip().split()))

        result = maximumSuperiorCharacters(freq)

        fptr.write(str(result) + '\n')

    fptr.close()


#by crazymerlin
#
#!/bin/python3

import os
import sys

# Complete the maximumSuperiorCharacters function below.
def maximumSuperiorCharacters(freq):
    pos = -1
    res = 0
    done = 0
    for f in freq:
        newres = res
        if pos > 0:
            added = min(pos, f)
            newres += added
            done += added
            pos -= added
            f -= added
        if res > 0:
            added = min(res*2, f) // 2 * 2
            newres += added // 2
            f -= added
        res = newres
        pos += f
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        freq = list(map(int, input().rstrip().split()))

        result = maximumSuperiorCharacters(freq)

        fptr.write(str(result) + '\n')

    fptr.close()