'''
Problem

Given a list of space separated words, reverse the order of the words.
Each line of text contains L letters and W words.
A line will only consist of letters and space characters.
There will be exactly one space character between each pair of consecutive words.

Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters
indicating a list of space separated words. Spaces will not appear at the start or end of a line.

Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

Limits

Small dataset

N = 5
1 ≤ L ≤ 25

Large dataset

N = 100
1 ≤ L ≤ 1000

Sample


Input

3
this is a test
foobar
all your base

Output
Case #1: test a is this
Case #2: foobar
Case #3: base your all

'''
import sys

def get_input_output_obj():
    lens = len(sys.argv)
    if lens >= 2:
        ins = open(sys.argv[1], "r")
        lines = [line for line in ins.readlines()]
        outs = open(sys.argv[2], "w")
        return (lines, outs)
    else:
        return (None, None)

inputs, outs = get_input_output_obj()
if inputs != None:
    test  = 1
    index = 0

    nb_test = int(inputs[index])
    index += 1

    for _ in range(nb_test):
        words = [x for x in inputs[index].split()]
        index += 1
        answer = []
        while words:
            answer.append(words.pop())
        ans1 = ' '.join(answer)
        ans  = "Case #{}: {}".format(test, ans1)
        print(ans, file = outs)
        test += 1
else:
    print("Invalid input.")



