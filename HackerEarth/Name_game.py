from string import ascii_letters as letters
from collections import OrderedDict

prime_ordinals = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
letter_arr = [0]*52
letter_dict = OrderedDict(zip(letters, letter_arr))
for key in letter_dict:
    if ord(key) in prime_ordinals:
        letter_dict[key] = key
vals = letter_dict.values()
valindx = list(vals)
for i, v in enumerate(valindx):
    if v == 0:
        l = i
        r = i
        while True:
            l -= 1
            if valindx[l]!= 0:
                letter_dict[letters[i]] = valindx[l]

                break
            r += 1

            if valindx[r]!= 0:
                letter_dict[letters[i]] = valindx[r]
                break

for _ in range(int(input())):
    input()
    s = input()
    for i in s:
        print(letter_dict[i],end="")
    print()






'''
SAMPLE INPUT
1
8
KINGKONG
SAMPLE OUTPUT
IIOGIOOG
'''




