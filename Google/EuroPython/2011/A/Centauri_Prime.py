'''
Problem
Back in the old days before the creation of the mighty Centauri Republic, the planet Centauri Prime
was split into several independent kingdoms. The kingdom of Mollaristan was ruled by king Loatold,
while the kingdom of Auritania was under the rule of queen Elana.
In fact, it just so happened that every kingdom whose name ended in a consonant was ruled by a king,
while every kingdom whose name ended in a vowel was ruled by a queen.
Also because of an amazing coincidence, all kingdoms whose named ended in the letter 'y' were
constantly in a state of turmoil and were not ruled by anyone.
Can you write a program that will determine the current rulers of several countries,
given the countries' names?

Input
The first line of the input gives the number of test cases, T.
T lines follow, each one containing the name of one country.
Country names will consist of only lower case English letters, starting with a capital letter.
There will be no other characters on any line, and no empty lines.

Output
For each test case, output one line containing "Case #x: C is ruled by Y.", where x is the
case number (starting from 1), C is the country name, and Y is either "a king", "a queen" or "nobody".
Be careful with capitalization and the terminating period. Your output must be in exactly this format.
See the examples below.

Limits
1 ≤ T ≤ 300.

Small dataset
Each country name will have between 3 and 20 letters.

Large dataset
Each country name will have at most 100 letters.

Sample

Input

3
Mollaristan
Auritania
Zizily

Output
Case #1: Mollaristan is ruled by a king.
Case #2: Auritania is ruled by a queen.
Case #3: Zizily is ruled by nobody.

'''
import sys

def get_input_output_object():
    args = sys.argv

    if len(args) >= 2:
        file_ins = open(sys.argv[1], "r")
        file_out = open(sys.argv[2], "w")
        return (file_ins, file_out)
    else:
        return (None, None)
def get_line(fobj):
    return fobj.readline().strip()

ins, out = get_input_output_object()
if ins is not None:
    test_nb = 1
    nb_test = int(get_line(ins))
    for _ in range(nb_test):
        name = get_line(ins)
        curr   = name[-1]
        if curr in "aeiouy" or curr in "AEIOUY":
            ans = "a queen."
            if curr == "y" or curr == "Y":
                ans = "nobody."
        else:
            ans = "a king."
        ans1 = "Case #{}: {} is ruled by {}".format(test_nb, name, ans)
        print(ans1, file = out)
        test_nb += 1
else:
    print("Invalid input output File.")