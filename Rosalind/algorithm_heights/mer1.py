from collections import Counter
import os


if __name__ == '__main__':
    # read data
    f =  open("rosalind_mer.txt", 'r')
    data = [map(int, line.rstrip().split()) for line in f.readlines()]

    A_len = data.pop(0)
    A = data.pop(0)
    B_len = data.pop(0)
    B = data.pop(0)

    C = A + B
    C.sort()

    # save output file
    outhandle = open("rosalind_mer_ans.txt",'w')
    print >> outhandle, " ".join(map(str, C))
    outhandle.close()