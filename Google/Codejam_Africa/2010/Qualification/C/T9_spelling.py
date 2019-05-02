'''
Problem

The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad.
We would like to make it easier to write a message to your friend using a sequence of keypresses
to indicate the desired characters. The letters are mapped onto the digits as shown below.
To insert the character B for instance, the program would press 22.
In order to insert two characters in sequence from the same key, the user must pause before
pressing the key a second time. The space character ' ' should be printed to indicate a pause.
For example, 2 2 indicates AA whereas 22 indicates B.

Input

The first line of input gives the number of cases, N. N test cases follow. Each case is a line of text formatted as

desired_message
Each message will consist of only lowercase characters a-z and space characters ' '. Pressing zero emits a space.

Output

For each test case, output one line containing "Case #x: " followed by the message translated into the sequence of keypresses.

Limits

1 ≤ N ≤ 100.

Small dataset

1 ≤ length of message in characters ≤ 15.

Large dataset

1 ≤ length of message in characters ≤ 1000.

Sample


Input


4
hi
yes
foo  bar
hello world

Output
Case #1: 44 444
Case #2: 999337777
Case #3: 333666 6660 022 2777
Case #4: 4433555 555666096667775553


'''
import sys


def get_word_symbol(words):
    dicts = {"0":" ", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
    last = ""
    symbol = ''
    for i in words:
        for j in dicts:
            if i in dicts[j]:
                curr = j * (dicts[j].index(i) + 1)
                if j == last:
                    symbol += " " + curr
                else:
                    symbol += curr
                last = j
    return symbol

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
        print(inputs[index])
        ans1 = get_word_symbol(inputs[index])

        index += 1
        ans = "Case #{}: {}".format(test, ans1)
        print(ans, file = outs)
        test += 1



else:
    print("Invalid input.")



